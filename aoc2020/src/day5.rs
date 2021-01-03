use std::fs;

pub fn run(input_file: &str) {
    let values = parse_input_file(input_file).unwrap();
    println!("part 1:  {:?}", part1(&values));
    // println!("part 2:  {:?}", part2(&values));
}

fn parse_input_file(file_name: &str) -> Result<Vec<String>, std::io::Error> {
    let contents = fs::read_to_string(file_name)?;
    let mut values: Vec<String> = Vec::new();

    for row in contents.split('\n') {
        if row.is_empty() {
            continue;
        }
        values.push(row.to_string());
    }

    return Ok(values);
}

fn part1(values: &Vec<String>) -> u32 {}
