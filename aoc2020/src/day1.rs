pub fn part1(values: Vec<i32>) -> i32{
    let desired_sum = 2020;

    for value1 in &values {
        for value2 in &values {
            if value1 + value2 == desired_sum {
                return value1 * value2;
            }
        }
    }

    return 0;
}
