use std::fs;

pub fn run(input_file: &str) {
    let values = parse_day1_input_file(input_file).unwrap();
    println!("part 1:  {}", part1(&values));
    println!("part 2:  {}", part2(&values));
}

fn parse_day1_input_file(file_name: &str) -> Result<Vec<i32>, std::io::Error> {
    let contents = fs::read_to_string(file_name)?;
    let mut values: Vec<i32> = Vec::new();
    for row in contents.split('\n') {
        if row.is_empty() {
            continue;
        }
        values.push(row.parse::<i32>().unwrap());
    }

    return Ok(values);
}

fn part1(values: &Vec<i32>) -> i32 {
    let desired_sum = 2020;

    for value1 in values {
        for value2 in values {
            if value1 + value2 == desired_sum {
                return value1 * value2;
            }
        }
    }

    return 0;
}

fn part2(values: &Vec<i32>) -> i32 {
    let desired_sum = 2020;

    for value1 in values {
        for value2 in values {
            for value3 in values {
                if value1 + value2 + value3 == desired_sum {
                    return value1 * value2 * value3;
                }
            }
        }
    }

    return 0;
}
