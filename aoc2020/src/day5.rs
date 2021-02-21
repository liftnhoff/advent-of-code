use std::fs;

pub fn run(input_file: &str) {
    let values = parse_input_file(input_file).unwrap();
    println!("part 1:  {:?}", part1(&values));
    // println!("part 2:  {:?}", part2(&values));
}

fn parse_input_file(file_name: &str) -> Result<Vec<String>, std::io::Error> {
    let contents = fs::read_to_string(file_name)?;
    let mut values: Vec<String> = Vec::new();

    for line in contents.split("\n") {
        if line.is_empty() {
            continue;
        }
        values.push(line.to_string());
    }

    return Ok(values);
}

fn part1(values: &Vec<String>) -> u32 {
    for seat in values {
        process_seat(seat);
    }
    return 1;
}

fn process_seat(seat: &String) -> u32 {
    let (row, col) = seat.split_at(7);
    // BFFFBBFRRR
    // FFFBBBFRRR
    // BBFFBBFRLL
    let mut row_min = 0;
    let mut row_max = 127;
    let lower_half_char = 'F';
    // let upper_half_char = 'B';
    for value in row.chars() {
        if value == lower_half_char {
            row_max = (row_max + row_min) / 2;
        } else {
            row_min = (row_max + row_min) / 2 + 1;
        }
        // println!("---");
        // println!("value:  {:?}", value);
        // println!("row_min:  {:?}", row_min);
        // println!("row_max:  {:?}", row_max);
    }
    println!("FOUND SEAT");
    println!("row_min:  {:?}", row_min);
    println!("row_max:  {:?}", row_max);
    println!("--------------");
    return row_min;

    // let mut col_min = 0;
    // let mut col_max = 7;

    // for character in seat.chars() {}
}
