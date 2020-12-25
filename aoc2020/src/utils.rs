use std::fs;

pub fn parse_file_of_ints(file_name: &str) -> Result<Vec<i32>, std::io::Error>{
    let contents = fs::read_to_string(file_name)?;
    let mut values: Vec<i32> = Vec::new();
    for row in contents.split('\n') {
        values.push(row.parse::<i32>().unwrap());
    }

    return Ok(values);
}
