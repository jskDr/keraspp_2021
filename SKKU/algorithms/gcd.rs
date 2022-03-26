

fn gcd(mut l:u32, mut s:u32)->u32{
    let mut r:u32;
    while s>0 {
        r = l % s;
        l = s;
        s = r;
    }
    l
}

fn main() {
    println!("{}", gcd(30,20));
}