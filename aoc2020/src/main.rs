mod day1;
mod day2;
mod day3;
mod utils;

use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    let day = &args[1];
    let input_file = &args[2];

    println!("{}", day);
    if day == "day1" {
        day1::run(input_file);
    } else if day == "day2" {
        let values = day2::parse_day2_input_file(input_file).unwrap();
        println!("part 1:  {:?}", day2::part1(&values));
        println!("part 2:  {:?}", day2::part2(&values));
    } else if day == "day3" {
        day3::run(input_file);
    }
}
