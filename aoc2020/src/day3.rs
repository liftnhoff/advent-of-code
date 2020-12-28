use std::fs;

pub fn run(input_file: &str) {
    let tree_map = parse_day3_input_file(input_file).unwrap();
    // tree_map.print();
    println!("part 1:  {:?}", part1(tree_map));
    // println!("part 2:  {:?}", part2(&values));
}

fn parse_day3_input_file(file_name: &str) -> Result<TreeMap, std::io::Error> {
    let contents = fs::read_to_string(file_name)?;
    let mut tree_map = TreeMap { rows: Vec::new() };

    let tree_marker = '#';
    for row in contents.split('\n') {
        if row.is_empty() {
            continue;
        }

        let mut tree_row = TreeRow { cols: Vec::new() };
        for character in row.chars() {
            if character == tree_marker {
                tree_row.cols.push(true);
            } else {
                tree_row.cols.push(false);
            }
        }
        tree_map.rows.push(tree_row);
    }

    return Ok(tree_map);
}

fn part1(tree_map: TreeMap) -> u32 {
    let steps_right_per_row = 3;
    let mut tree_count: u32 = 0;
    let mut col_index = 0;
    for tree_row in &tree_map.rows {
        if tree_row.has_tree(col_index) {
            tree_count += 1;
        }
        col_index += steps_right_per_row;
    }
    return tree_count;
}

// fn part2(passwords_and_policies: &Vec<PasswordAndPolicy>) -> u32 {

// }

struct TreeMap {
    rows: Vec<TreeRow>,
}

impl TreeMap {
    fn has_tree(&self, row_index: usize, col_index: usize) -> bool {
        return self.rows.get(row_index).unwrap().has_tree(col_index);
    }

    fn print(&self) {
        for tree_row in &self.rows {
            tree_row.print();
        }
    }
}

struct TreeRow {
    cols: Vec<bool>,
}

impl TreeRow {
    fn has_tree(&self, col_index: usize) -> bool {
        let index = col_index % self.cols.len();
        return *self.cols.get(index).unwrap_or(&false);
    }

    fn print(&self) {
        let line: String = self
            .cols
            .iter()
            .map(|&v| if v { "#" } else { "." })
            .collect();
        println!("{}", line);
    }
}
