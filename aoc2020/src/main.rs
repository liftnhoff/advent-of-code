mod day1;
mod utils;

use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    let day = &args[1];
    let input_file = &args[2];

    if day == "day1" {
        println!("made it here");
        let values = utils::parse_file_of_ints("input_data/example_day1.txt");
        for value in values {
            println!("{}", value.to_string());
        }
        day1::part1();
    }

    
}
