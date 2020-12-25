mod day1;
mod utils;

use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    let day = &args[1];
    let input_file = &args[2];

    println!("{:?}", day);
    if day == "day1" {
        let values = utils::parse_file_of_ints(input_file).unwrap();
        println!("part 1:  {:?}", day1::part1(&values));
        println!("part 2:  {:?}", day1::part2(&values));
    }
    
}
