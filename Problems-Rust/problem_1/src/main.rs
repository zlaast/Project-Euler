// Project Euler: Problem 1
// Multiples of 3 or 5
// Alternate Rust version

fn main() {
    let mut sum = 0;
    for number in 3..1000 {
        if number % 3 == 0 || number % 5 == 0 {
            sum += number;
        }
    }

    println!("{}", sum);
}