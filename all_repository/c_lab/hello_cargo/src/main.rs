fn prod_vec() -> Vec<i32> {
    vec![1, 2, 3]
}

fn main() {
    println!("Hello, world!");

    // sum from 0 to 9
    let s = (0..10).sum::<i32>();
    println!("Sum from 0 to 9 using sum: {}", s);

    // sum from 0 to 9 using fold
    let s = (0..10).fold(0, |acc, x| acc + x);
    println!("Sum from 0 to 9 using fold: {}", s);

    // make a vec
    let v = prod_vec();
    println!("Vec: {:?}", v);

    // make a vec with a default value
    let v = vec![1,2,3];
    println!("Vec: {:?}", v);
}
