fn fibo(n: i32) -> i32 {
    if n < 2 {
        n
    } else {
        fibo(n-1) + fibo(n-2)
    }
}

fn main() {
    println!("{}", fibo(45))
}