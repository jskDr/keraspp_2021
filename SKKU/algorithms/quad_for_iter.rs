

fn main() {
    let mut sum:isize = 0;
    let n:isize = 10;
    for i in 0..n {
        for j in 0..i { 
            for _k in 0..j {
                sum += 1;
            }
        }
    }

    println!("Total complexiity: {}", sum);
}

