#[derive(Debug)]
struct Point {
    x: i32,
    y: i32
}

fn test1() {
    let p1 = Point {x: 1, y: 2};
    // println!("({},{})", p1.x, p1.y);
    println!("{:?}", p1);
}

fn main() {
    test1();
}
