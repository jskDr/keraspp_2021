use rand::Rng; // 0.8.5
use std::io; 

fn main() {
    println!("GuGuDan Game");
    println!("============");
    while(true) {
        let (a, b) = show_problem();
        let answer = ask_answer();
        provide_result(a, b, answer);
        if !ask_again() {
            break;
        }
    }
}

fn ask_again() -> bool {
    println!("Do you want to play again? (y/n)");
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    input.trim() == "y"
}

fn show_problem() -> (i32, i32) {
    // print without new line
    println!("Answer to this problem: ");
    let a = rand::thread_rng().gen_range(1..10);
    let b = rand::thread_rng().gen_range(1..10);
    println!("{} x {} = ? ", a, b);
    return (a, b);
}

fn ask_answer() -> i32 {
    let mut answer = String::new();
    io::stdin()
        .read_line(&mut answer)
        .expect("Failed to read line");
    // convert Str to int
    return answer.trim().parse::<i32>().unwrap();
}

fn provide_result(a: i32, b: i32, answer: i32) {
    println!("Answer: {} x {} = {}", a, b, a * b);
    print!("Your answer of {} is ", answer);
    if answer == a * b {
        println!("Correct!");
    } else {
        println!("Wrong!");
    }
}