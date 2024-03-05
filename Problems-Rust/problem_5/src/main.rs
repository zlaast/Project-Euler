// Project Euler: Problem 5
// Smallest Multiple
// Alternate Rust version

use std::collections::HashSet;

fn main() {
    let mut product: i32 = 1;
    let primes = vec![2, 3, 5, 7, 11, 13, 17, 19];

    for i in 2..=20 {
        let mut num = i;
        let mut list = HashSet::new();

        // Steps 1 and 2: Perform prime factorization
        // on each number and discard duplicate factors
        for prime in primes.iter() {
            while num % prime == 0 {
                num = num / prime;
                list.insert(prime);
            }
        }

        // Steps 3 and 4: Discard factorizations with 
        // different numbers and multiply all factors
        if list.len() == 1 {
            let factor: i32 = *Vec::from_iter(list)[0];
            product = product * factor;
        }
    }

    println!("{}", product);
}