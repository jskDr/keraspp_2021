fn move_hanoi(n: i32, from: i32, to: i32, via: i32) {
    if n > 0 {
        move_hanoi(n - 1, from, via, to);
        println!("n = {}: Move disk from pole {} to pole {}", n, from, to);
        move_hanoi(n - 1, via, to, from);
    }
}

use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    println!("{:?}", args);
    
    let n = args[1].parse::<i32>().unwrap();
    let from = args[2].parse::<i32>().unwrap();
    let to = args[3].parse::<i32>().unwrap();
    let via = args[4].parse::<i32>().unwrap();

    println!("{},{},{},{}", n, from, to, via);
    move_hanoi(n, from, to, via);
}