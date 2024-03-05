// Project Euler: Problem 4
// Largest Palindrome Product
// Alternate Rust version

fn main() {
    let mut max = 0;

    for a in 100..1000 {
        for b in a..1000 {
            let product = a*b;
            let f_string: String = format!("{}", product);
            let r_string: String = f_string.chars().rev().collect();

            if f_string == r_string && product > max {
                max = product;
            }
        }
    }

    println!("{}", max);
}