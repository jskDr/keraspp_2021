use std::env;

fn main() {
    println!("Hello");

    let args: Vec<String> = env::args().collect();
    println!("{:?}", args);

    // let mut avec: Vec<usize>;
    if args.len() == 2 {
        let n: usize = args[1].parse().unwrap();
        let mut avec = Vec::with_capacity(n);
        for _ in 0..n {
            avec.push(0)
        }
        println!("{:?}", avec);
    }
}

