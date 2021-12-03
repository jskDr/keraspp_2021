fn main() {
    println!("Hello, world!");

    test_sum_all();
    test_prod();
    test_sum_vec_move();
    test_sum_vec_borrow();
}

// ===============================================================
fn test_sum_vec_borrow() {
    let data = vec![1, 3, 5];
    println!("{:?}", data);

    let s = sum_vec_borrow(&data);
    println!("Sum of {:?} is {}", data, s);
    // println!("Sum is {}", s);
}

fn sum_vec_borrow(data: &Vec<i32>) -> i32 {
    // data.iter().sum()
    let mut s: i32 = 0;
    for d in data.iter() {
        s += d;
    }
    s
}

// ===============================================================
fn test_sum_vec_move() {
    let data = vec![1, 3, 5];
    println!("{:?}", data);

    let s = sum_vec_move(data);
    // println!("Sum of {:?} is {}", data, s);
    println!("Sum is {}", s);
}

fn sum_vec_move(data: Vec<i32>) -> i32 {
    data.iter().sum()
}

// ===============================================================
fn test_prod() {
    let n: i32 = 5;
    let r = prod(n);
    println!("Factorial of {} is given to {}", n, r);
}

fn prod(n: i32) -> i32 {
    if n <= 1 {
        1
    } else {
        n * prod(n-1)
    }
}

// ===============================================================
fn test_sum_all() {
    let n: u32 = 10;
    println!("This is sum of 0..{}", n);
    let s = sum_all(n);
    println!("Sum is {}", s);
}

fn sum_all(n: u32) -> u32 {
    let mut s: u32 = 0;
    for i in 0..n {
        s += i;
    }
    s
} 