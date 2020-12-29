use std::collections::HashMap;
use std::fs;

pub fn run(input_file: &str) {
    let passports = parse_input_file(input_file).unwrap();
    println!("part 1:  {:?}", part1(&passports));
    // println!("part 2:  {:?}", part2(&passports));
}

fn parse_input_file(file_name: &str) -> Result<Vec<HashMap<String, String>>, std::io::Error> {
    let contents = fs::read_to_string(file_name)?;
    let mut passports: Vec<HashMap<String, String>> = Vec::new();

    for data in contents.split("\n\n") {
        if data.is_empty() {
            continue;
        }

        let mut passport: HashMap<String, String> = HashMap::new();
        for kv_string in data.split_whitespace() {
            let mut key_and_value = kv_string.split(":");
            let key = key_and_value.next().unwrap().to_string();
            let value = key_and_value.next().unwrap().to_string();
            passport.insert(key, value);
        }
        passports.push(passport);
    }

    return Ok(passports);
}

fn part1(passports: &Vec<HashMap<String, String>>) -> u32 {
    let required_keys = [
        "byr".to_string(),
        "iyr".to_string(),
        "eyr".to_string(),
        "hgt".to_string(),
        "hcl".to_string(),
        "ecl".to_string(),
        "pid".to_string(),
    ];

    let mut valid_count = 0;
    for passport in passports {
        let mut is_valid = true;
        for key in &required_keys {
            if !passport.contains_key(key) {
                is_valid = false;
                break;
            }
        }

        if is_valid {
            valid_count += 1;
        }
    }

    return valid_count;
}

// fn part2(tree_map: &TreeMap) -> u64 {}
