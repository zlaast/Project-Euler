// Project Euler: Problem 9
// Special Pythagorean Triplet
// Alternate Rust version

fn main() {
    'outer: for n in 1_i32..=500 {
        for m in (n+1)..=500 {
            if m*(m+n) == 500 {
                let a: i32 = m.pow(2) - n.pow(2);
                let b: i32 = 2*m*n;
                let c: i32 = m.pow(2) + n.pow(2);

                println!("{}", a*b*c);
                break 'outer;
            }
        }
    }
}