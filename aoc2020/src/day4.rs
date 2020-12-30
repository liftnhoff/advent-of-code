use std::collections::HashMap;
use std::fs;

pub fn run(input_file: &str) {
    let passports = parse_input_file(input_file).unwrap();
    println!("part 1:  {:?}", part1(&passports));
    // println!("part 2:  {:?}", part2(&passports));
}

fn parse_input_file(file_name: &str) -> Result<Vec<Passport>, std::io::Error> {
    let contents = fs::read_to_string(file_name)?;
    let mut passports: Vec<Passport> = Vec::new();

    for data in contents.split("\n\n") {
        if data.is_empty() {
            continue;
        }

        let mut passport = create_passport();
        for kv_string in data.split_whitespace() {
            let mut key_and_value = kv_string.split(":");
            let key = key_and_value.next().unwrap().to_string();
            let value = key_and_value.next().unwrap().to_string();
            passport.add_field(key, value);
        }
        passports.push(passport);
    }

    return Ok(passports);
}

fn create_passport() -> Passport {
    return Passport {
        fields: HashMap::new(),
    };
}

/*
Use the `create_passport` function to instantiate a Passport instead of creating one directly.
 */
struct Passport {
    fields: HashMap<String, String>,
}

const PASSPORT_REQUIRED_KEYS: [&str; 7] = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"];

impl Passport {
    fn add_field(&mut self, key: String, value: String) {
        self.fields.insert(key, value);
    }

    fn is_valid_part1(&self) -> bool {
        let mut is_valid = true;
        for key in &PASSPORT_REQUIRED_KEYS {
            if !self.fields.contains_key(*key) {
                is_valid = false;
                break;
            }
        }

        return is_valid;
    }

    // fn is_valid_part2(&self) -> bool {
    //     let REQUIRED_KEYS = [
    //         "byr".to_string(),
    //         "iyr".to_string(),
    //         "eyr".to_string(),
    //         "hgt".to_string(),
    //         "hcl".to_string(),
    //         "ecl".to_string(),
    //         "pid".to_string(),
    //     ];
    // }
}

fn part1(passports: &Vec<Passport>) -> u32 {
    let mut valid_count = 0;
    for passport in passports {
        if passport.is_valid_part1() {
            valid_count += 1;
        }
    }

    return valid_count;
}

// fn part2(tree_map: &TreeMap) -> u64 {}
