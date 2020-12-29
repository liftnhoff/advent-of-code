use std::fs;

pub fn run(input_file: &str) {
    let tree_map = parse_input_file(input_file).unwrap();
    // tree_map.print();
    println!("part 1:  {:?}", part1(&tree_map));
    println!("part 2:  {:?}", part2(&tree_map));
}

fn parse_input_file(file_name: &str) -> Result<TreeMap, std::io::Error> {
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

fn part1(tree_map: &TreeMap) -> u32 {
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

fn part2(tree_map: &TreeMap) -> u64 {
    let steps_right_per_row = [1, 3, 5, 7];
    let mut tree_count_per_row = [0, 0, 0, 0];
    let mut col_indices_per_row = [0, 0, 0, 0];

    let steps_right_per_two_rows = [1];
    let mut tree_count_per_two_rows = [0];
    let mut col_indices_per_two_rows = [0];

    for (row_index, tree_row) in tree_map.rows.iter().enumerate() {
        for count_index in 0..tree_count_per_row.len() {
            if tree_row.has_tree(col_indices_per_row[count_index]) {
                tree_count_per_row[count_index] += 1;
            }
            col_indices_per_row[count_index] += steps_right_per_row[count_index];
        }

        if row_index % 2 == 0 {
            for count_index in 0..tree_count_per_two_rows.len() {
                if tree_row.has_tree(col_indices_per_two_rows[count_index]) {
                    tree_count_per_two_rows[count_index] += 1;
                }
                col_indices_per_two_rows[count_index] += steps_right_per_two_rows[count_index];
            }
        }
    }

    let mut result: u64 = 1;
    for value in &tree_count_per_row {
        result *= value;
    }
    for value in &tree_count_per_two_rows {
        result *= value;
    }

    return result;
}

struct TreeMap {
    rows: Vec<TreeRow>,
}

// impl TreeMap {
//     fn has_tree(&self, row_index: usize, col_index: usize) -> bool {
//         return self.rows.get(row_index).unwrap().has_tree(col_index);
//     }
//
//     fn print(&self) {
//         for tree_row in &self.rows {
//             tree_row.print();
//         }
//     }
// }

struct TreeRow {
    cols: Vec<bool>,
}

impl TreeRow {
    fn has_tree(&self, col_index: usize) -> bool {
        let index = col_index % self.cols.len();
        return *self.cols.get(index).unwrap_or(&false);
    }

    // fn print(&self) {
    //     let line: String = self
    //         .cols
    //         .iter()
    //         .map(|&v| if v { "#" } else { "." })
    //         .collect();
    //     println!("{}", line);
    // }
}
