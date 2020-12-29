mod day1;
mod day2;
mod day3;

use regex::Regex;
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    let input_file = &args[1];

    let day_regex = Regex::new(r"(day\d{1,2})").unwrap();
    let cap = day_regex.captures(input_file);
    if cap.is_none() {
        println!("Could not identify day number from input file name.");
        return;
    }
    let day = &cap.unwrap()[1];

    println!("{}", day);
    if day == "day1" {
        day1::run(input_file);
    } else if day == "day2" {
        day2::run(input_file);
    } else if day == "day3" {
        day3::run(input_file);
    }
}
