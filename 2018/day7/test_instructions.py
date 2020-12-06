import pytest

from .instructions import (
    CircularInstructionsError, DataError, StartingNodeError,
    Instructions, StepNode,
)

#('GRWKBEVZDSYAPMTUCFIXQJLHNO', 903)


class TestInstructions:
    def test_read_instructions_bad_data(self):
        with pytest.raises(DataError):
            Instructions.read_instructions(__file__)

    def test__add_instruction(self):
        instructions = Instructions()

        instructions._add_instruction('a', 'b')
        assert instructions.step_nodes['a'].parents == set()
        assert instructions.step_nodes['a'].children == {instructions.step_nodes['b']}
        assert instructions.step_nodes['b'].parents == {instructions.step_nodes['a']}
        assert instructions.step_nodes['b'].children == set()
        assert instructions.starting_nodes == {instructions.step_nodes['a']}

        instructions._add_instruction('b', 'c')
        assert instructions.step_nodes['b'].parents == {instructions.step_nodes['a']}
        assert instructions.step_nodes['b'].children == {instructions.step_nodes['c']}
        assert instructions.step_nodes['c'].parents == {instructions.step_nodes['b']}
        assert instructions.step_nodes['c'].children == set()
        assert instructions.starting_nodes == {instructions.step_nodes['a']}

        instructions._add_instruction('d', 'a')
        assert instructions.step_nodes['d'].parents == set()
        assert instructions.step_nodes['d'].children == {instructions.step_nodes['a']}
        assert instructions.step_nodes['a'].parents == {instructions.step_nodes['d']}
        assert instructions.step_nodes['a'].children == {instructions.step_nodes['b']}
        assert instructions.starting_nodes == {instructions.step_nodes['d']}

    def test_determine_step_order(self):
        instructions = Instructions.read_instructions('day7/data/test_data.txt')
        assert instructions.determine_step_order() == 'CABDFE'

    def test_determine_step_order_circular_instructions(self):
        instructions = Instructions()
        instructions._add_instruction('a', 'b')
        instructions._add_instruction('b', 'c')
        instructions._add_instruction('c', 'a')
        with pytest.raises(StartingNodeError):
            instructions.determine_step_order()

        instructions._add_instruction('d', 'a')
        with pytest.raises(CircularInstructionsError):
            instructions.determine_step_order()

    def test_determine_step_order_with_time(self):
        instructions = Instructions.read_instructions('day7/data/test_data.txt')
        step_duration_base = 0
        worker_count = 1
        assert instructions.determine_step_order_with_time(
            step_duration_base, worker_count
        )[0] == 'CABDFE'

        step_duration_base = 0
        worker_count = 2
        assert instructions.determine_step_order_with_time(
            step_duration_base, worker_count
        ) == ('CABFDE', 15)


class TestStepNode:
    def test_add_parent(self):
        step_a = StepNode('a')
        step_b = StepNode('b')

        step_a.add_parent(step_b)
        assert step_a.parents == {step_b}

        step_a.add_parent(step_b)
        assert step_a.parents == {step_b}

    def test_add_child(self):
        step_a = StepNode('a')
        step_b = StepNode('b')

        step_a.add_child(step_b)
        assert step_a.children == {step_b}

        step_a.add_child(step_b)
        assert step_a.children == {step_b}
