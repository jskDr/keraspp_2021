struct Point {
    x: i32,
    y: i32
}

impl std::fmt::Display for Point {
    fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
        write!(f, "Point({}, {})", self.x, self.y)
    }
}

fn test1() {
    let p1 = Point {x: 1, y: 2};
    println!("{}", p1);
}

fn main() {
    test1();
}
