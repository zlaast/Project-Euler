// Project Euler: Problem 2
// Even Fibonacci Numbers
// Alternate Rust version

fn main() {
    let mut f_p = 0;     // Previous Fibonacci number
    let mut f_c = 1;     // Current Fibonacci number
    let mut sum = 0;

    while f_c < 4000000 {
        let f_n = f_c + f_p;   // f_n is the next Fibonacci number

        if f_n % 2 == 0 {
            sum += f_n;
        }

        f_p = f_c;
        f_c = f_n;
    }

    println!("{}", sum);
}