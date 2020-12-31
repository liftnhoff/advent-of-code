use regex::Regex;
use std::collections::HashMap;
use std::collections::HashSet;
use std::fs;

pub fn run(input_file: &str) {
    let passports = parse_input_file(input_file).unwrap();
    println!("part 1:  {:?}", part1(&passports));
    println!("part 2:  {:?}", part2(&passports));
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

    fn is_valid_part2(&self) -> bool {
        let mut is_valid = true;
        for key in &PASSPORT_REQUIRED_KEYS {
            if !self.fields.contains_key(*key) {
                is_valid = false;
                break;
            }

            let value_option = self.fields.get(*key);
            if value_option.is_none() {
                is_valid = false;
                break;
            }
            let value = value_option.unwrap();

            if *key == "byr" {
                is_valid = self._is_valid_byr(value);
            } else if *key == "iyr" {
                is_valid = self._is_valid_iyr(value);
            } else if *key == "eyr" {
                is_valid = self._is_valid_eyr(value);
            } else if *key == "hgt" {
                is_valid = self._is_valid_hgt(value);
            } else if *key == "hcl" {
                is_valid = self._is_valid_hcl(value);
            } else if *key == "ecl" {
                is_valid = self._is_valid_ecl(value);
            } else if *key == "pid" {
                is_valid = self._is_valid_pid(value);
            }

            if !is_valid {
                break;
            }
        }

        return is_valid;
    }

    fn _is_valid_byr(&self, value: &String) -> bool {
        // byr (Birth Year) - four digits; at least 1920 and at most 2002.
        return self._is_valid_year(value, 1920, 2002);
    }

    fn _is_valid_iyr(&self, value: &String) -> bool {
        // iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        return self._is_valid_year(value, 2010, 2020);
    }

    fn _is_valid_eyr(&self, value: &String) -> bool {
        // eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        return self._is_valid_year(value, 2020, 2030);
    }

    fn _is_valid_year(&self, value: &String, min: u32, max: u32) -> bool {
        if value.len() != 4 {
            return false;
        }
        let year_result = value.parse::<u32>();
        if year_result.is_err() {
            return false;
        }
        let year = year_result.unwrap();
        if year < min || year > max {
            return false;
        }
        return true;
    }

    fn _is_valid_hgt(&self, value: &String) -> bool {
        /*
        hgt (Height) - a number followed by either cm or in:

        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
         */
        let re = Regex::new(r"^(\d+)((in)|(cm))$").unwrap();
        let cap_result = re.captures(value.as_str());
        if cap_result.is_none() {
            return false;
        }
        let cap = cap_result.unwrap();
        let number = cap
            .get(1)
            .map_or(0, |x| x.as_str().parse::<usize>().unwrap());
        let units = cap.get(2).map_or("", |x| x.as_str());

        if units == "in" {
            if number < 59 || number > 76 {
                return false;
            }
        } else if units == "cm" {
            if number < 150 || number > 193 {
                return false;
            }
        } else {
            return false;
        }
        return true;
    }

    fn _is_valid_hcl(&self, value: &String) -> bool {
        // hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        let re = Regex::new(r"^#[0-9a-f]{6}$").unwrap();
        let cap_result = re.captures(value.as_str());
        if cap_result.is_none() {
            return false;
        }
        return true;
    }

    fn _is_valid_ecl(&self, value: &String) -> bool {
        // ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        let valid_ecl_values: HashSet<&'static str> =
            ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
                .iter()
                .cloned()
                .collect();
        return valid_ecl_values.contains(value.as_str());
    }

    fn _is_valid_pid(&self, value: &String) -> bool {
        // pid (Passport ID) - a nine-digit number, including leading zeroes.
        let re = Regex::new(r"^\d{9}$").unwrap();
        let cap_result = re.captures(value.as_str());
        if cap_result.is_none() {
            return false;
        }
        return true;
    }
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

fn part2(passports: &Vec<Passport>) -> u32 {
    let mut valid_count = 0;
    for passport in passports {
        if passport.is_valid_part2() {
            valid_count += 1;
        }
    }

    return valid_count;
}
