// Project Euler: Problem 6
// Sum square difference
// Alternate Rust version

fn main() {
    let n = 100;

    let a: i32 = n*(n+1);
    let sum_square: i32 = (a*(2*n + 1))/6;
    let square_sum: i32 = (a/2).pow(2);

    println!("{}", square_sum - sum_square);
}