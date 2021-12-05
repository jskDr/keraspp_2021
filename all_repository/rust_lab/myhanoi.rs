use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    println!("{:?}", args);
    
    if args.len() == 5 {
        let n = args[1].parse::<usize>().unwrap();
        let from = args[2].parse::<usize>().unwrap();
        let to = args[3].parse::<usize>().unwrap();
        let via = args[4].parse::<usize>().unwrap();
        println!("{},{},{},{}", n, from, to, via);
        move_hanoi(n, from, to, via);
    }
    println!("Please use: myhanoi n from to via");
}

fn move_hanoi(n: usize, from: usize, to: usize, via: usize) {
    // println!("{},{},{},{}", n, from, to, via);
    if n > 0 {
        move_hanoi(n-1, from, via, to);
        println!("n={}: Moving from {} to {}", n, from, to);
        move_hanoi(n-1, via, to, from);
    }
}