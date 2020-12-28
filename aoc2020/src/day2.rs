use regex::Regex;
use std::fs;

pub fn run(input_file: &str) {
    let values = parse_day2_input_file(input_file).unwrap();
    println!("part 1:  {}", part1(&values));
    println!("part 2:  {}", part2(&values));
}

fn parse_day2_input_file(file_name: &str) -> Result<Vec<PasswordAndPolicy>, std::io::Error> {
    let contents = fs::read_to_string(file_name)?;
    let mut values: Vec<PasswordAndPolicy> = Vec::new();

    let re = Regex::new(r"^(\d+)-(\d+) (\w): (\w+)$").unwrap();
    for row in contents.split('\n') {
        if row.is_empty() {
            continue;
        }

        let cap = re.captures(row).unwrap();
        if cap.len() > 1 {
            let value = PasswordAndPolicy {
                count_min: cap
                    .get(1)
                    .map_or(0, |x| x.as_str().parse::<usize>().unwrap()),
                count_max: cap
                    .get(2)
                    .map_or(0, |x| x.as_str().parse::<usize>().unwrap()),
                required_character: cap
                    .get(3)
                    .map_or(String::from(""), |x| x.as_str().to_string()),
                password: cap
                    .get(4)
                    .map_or(String::from(""), |x| x.as_str().to_string()),
            };
            values.push(value);
        }
    }

    return Ok(values);
}

struct PasswordAndPolicy {
    count_min: usize,
    count_max: usize,
    required_character: String,
    password: String,
}

impl PasswordAndPolicy {
    fn is_valid_password_part1(&self) -> bool {
        let occurrence_count = self.password.matches(&self.required_character).count();
        if occurrence_count >= self.count_min && occurrence_count <= self.count_max {
            return true;
        } else {
            return false;
        }
    }

    fn is_valid_password_part2(&self) -> bool {
        let mut found_required_char = false;
        let required_char = self.required_character.chars().next().unwrap();
        for (index, character) in self.password.chars().enumerate() {
            if index == self.count_min - 1 || index == self.count_max - 1 {
                if character == required_char {
                    found_required_char = !found_required_char;
                }
            }
        }
        return found_required_char;
    }
}

fn part1(passwords_and_policies: &Vec<PasswordAndPolicy>) -> u32 {
    let mut count = 0;
    for password_and_policy in passwords_and_policies {
        if password_and_policy.is_valid_password_part1() {
            count += 1;
        }
    }
    return count;
}

fn part2(passwords_and_policies: &Vec<PasswordAndPolicy>) -> u32 {
    let mut count = 0;
    for password_and_policy in passwords_and_policies {
        if password_and_policy.is_valid_password_part2() {
            count += 1;
        }
    }
    return count;
}
