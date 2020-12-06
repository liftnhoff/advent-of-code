import re


class DataError(Exception):
    pass


class CircularInstructionsError(Exception):
    pass


class StartingNodeError(Exception):
    pass


class Instructions:
    def __init__(self):
        self.step_nodes = {}
        self.starting_nodes = set()

    @classmethod
    def read_instructions(cls, data_file):
        """Read instruction steps from a file.

        Args:
            data_file (str): The path to a file containing newline separated instruction
                dependencies. Each line should have the form
                    `Step C must be finished before step A can begin.`
                where C and A are steps to be completed.

        Returns:
            Instructions: The collection of points specified in the data_file.
        """
        step_regex = re.compile(
            r'^Step (\w+) must be finished before step (\w+) can begin.'
        )
        instructions = Instructions()
        with open(data_file) as fid:
            for line in fid:
                match = step_regex.match(line)
                try:
                    parent_id = match.group(1)
                    child_id = match.group(2)
                except AttributeError:
                    raise DataError(
                        f'Input data file line does not match expected pattern.'
                        f' Line: {line}'
                    )
                instructions._add_instruction(parent_id, child_id)

        return instructions

    def _add_instruction(self, parent_step_id, child_step_id):
        if parent_step_id not in self.step_nodes:
            self.step_nodes[parent_step_id] = StepNode(parent_step_id)
            self.starting_nodes.add(self.step_nodes[parent_step_id])

        if child_step_id not in self.step_nodes:
            self.step_nodes[child_step_id] = StepNode(child_step_id)

        self.step_nodes[parent_step_id].add_child(self.step_nodes[child_step_id])
        self.step_nodes[child_step_id].add_parent(self.step_nodes[parent_step_id])

        if self.step_nodes[child_step_id] in self.starting_nodes:
            self.starting_nodes.remove(self.step_nodes[child_step_id])

    def determine_step_order(self):
        """Determine the order that the instruction steps must be completed in.
        Steps with the same order rank will have a secondary alphabetical sort
        applied.

        Returns:
            str: A string containing the ordered instruction steps.
        """
        if not self.starting_nodes:
            raise StartingNodeError('There are no starting nodes.')

        step_orderer = _StepOrderer(self.starting_nodes)
        step_order = step_orderer.process()

        if len(step_order) != len(self.step_nodes):
            raise CircularInstructionsError(
                'Could not order steps. Check for circular instructions.'
            )

        return ''.join([step.identifier for step in step_order])

    def determine_step_order_with_time(self, step_duration_base, worker_count):
        """Determine the order that steps should be completed and how long
        it will take to complete them.

        Args:
            step_duration_base (int): The base amount of time each step takes.
            worker_count (int): The number of concurrent workers following the
                instructions.

        Returns:
            tuple(str, int): A tuple of completion order and how long the
                instructions will take.
        """
        if not self.starting_nodes:
            raise StartingNodeError('There are no starting nodes.')

        step_orderer = _StepOrdererTimed(
            self.starting_nodes, step_duration_base, worker_count
        )
        step_order, duration = step_orderer.process()

        if len(step_order) != len(self.step_nodes):
            raise CircularInstructionsError(
                'Could not order steps. Check for circular instructions.'
            )

        return (
            ''.join([step.identifier for step in step_order]),
            duration,
        )


class StepNode:
    """A step in a set of instructions with potential precursor (parent) steps
    and potential following (child) steps.
    """
    def __init__(self, identifier):
        self.identifier = identifier

        self.parents = set()
        self.children = set()
        self.remaining_time = None

    def __str__(self):
        return f'StepNode.{self.identifier}'

    def __repr__(self):
        return str(self)

    def add_parent(self, step_node):
        self.parents.add(step_node)

    def add_child(self, step_node):
        self.children.add(step_node)


class _StepOrderer:
    def __init__(self, starting_nodes):
        self.starting_nodes = starting_nodes

        self.step_order = []
        self.available_steps = set(self.starting_nodes)
        self.completed_steps = set()

    def process(self):
        while self.available_steps:
            step = sorted(self.available_steps, key=lambda x: x.identifier)[0]
            self.step_order.append(step)
            self.completed_steps.add(step)
            self.available_steps.remove(step)
            self.available_steps.update(self._get_newly_available_steps(step))

        return self.step_order

    def _get_newly_available_steps(self, step):
        newly_available_steps = set()
        for child in step.children:
            if child.parents.issubset(self.completed_steps):
                newly_available_steps.add(child)

        return newly_available_steps


class _StepOrdererTimed(_StepOrderer):
    _STEP_DURATIONS = {
        step: duration
        for duration, step in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ', start=1)
    }

    def __init__(self, starting_nodes, step_duration_base, worker_count):
        super().__init__(starting_nodes)

        self.step_duration_base = step_duration_base
        self.worker_count = worker_count

        self.current_steps = set()
        self.duration = 0

    def process(self):
        while self.available_steps or self.current_steps:
            self._queue_available_steps()
            self._do_work()
            self._mark_completed_steps()

        return self.step_order, self.duration

    def _queue_available_steps(self):
        available_workers = self.worker_count - len(self.current_steps)
        if not available_workers:
            return

        sorted_available = sorted(self.available_steps, key=lambda x: x.identifier)
        for step in sorted_available[:available_workers]:
            step.remaining_time = (
                self.step_duration_base + self._STEP_DURATIONS[step.identifier]
            )
            self.current_steps.add(step)
            self.available_steps.remove(step)

    def _do_work(self):
        self.duration += 1

    def _mark_completed_steps(self):
        for step in list(self.current_steps):
            step.remaining_time -= 1
            if step.remaining_time <= 0:
                self.current_steps.remove(step)
                self.completed_steps.add(step)
                self.step_order.append(step)
                self.available_steps.update(self._get_newly_available_steps(step))
