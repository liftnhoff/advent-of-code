use std::fs;

pub fn run(input_file: &str) {
    let values = parse_input_file(input_file).unwrap();
    println!("part 1:  {:?}", part1(&values));
    println!("part 2:  {:?}", part2(&values));
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

fn part1(values: &Vec<String>) -> i32 {
    let mut seat_id_max = 0;
    for seat in values {
        let seat_id = calculate_seat_id(seat);
        if seat_id > seat_id_max {
            seat_id_max = seat_id;
        }
    }
    return seat_id_max;
}

fn part2(values: &Vec<String>) -> i32 {
    let mut seat_ids: Vec<i32> = Vec::new();
    for seat in values {
        seat_ids.push(calculate_seat_id(seat));
    }

    seat_ids.sort();

    let mut prev_seat_id = 2147483647;
    let mut result = 0;
    for seat_id in seat_ids {
        if (seat_id - prev_seat_id) > 1 {
            result = prev_seat_id + 1;
            break;
        }
        prev_seat_id = seat_id;
    }

    return result;
}

fn calculate_seat_id(seat: &String) -> i32 {
    let (row, col) = seat.split_at(7);
    let row_value = calculate_seat_row_value(row);
    let col_value = calculate_seat_col_value(col);
    let row_multiplier = 8;
    return row_value * row_multiplier + col_value;
}

fn calculate_seat_row_value(row: &str) -> i32 {
    let mut row_min = 0;
    let mut row_max = 127;
    let lower_half_char = 'F'; // upper_half_char = 'B';
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

    if row_min != row_max {
        println!("ROW MIN AND MAX DO NOT MATCH");
        println!("row_min:  {:?}", row_min);
        println!("row_max:  {:?}", row_max);
    }

    return row_min;
}

fn calculate_seat_col_value(col: &str) -> i32 {
    let mut col_min = 0;
    let mut col_max = 7;
    let lower_half_char = 'L'; // upper_half_char = 'R';
    for value in col.chars() {
        if value == lower_half_char {
            col_max = (col_max + col_min) / 2;
        } else {
            col_min = (col_max + col_min) / 2 + 1;
        }
        // println!("---");
        // println!("value:  {:?}", value);
        // println!("col_min:  {:?}", col_min);
        // println!("col_max:  {:?}", col_max);
    }

    if col_min != col_max {
        println!("COL MIN AND MAX DO NOT MATCH");
        println!("col_min:  {:?}", col_min);
        println!("col_max:  {:?}", col_max);
    }

    return col_min;
}
