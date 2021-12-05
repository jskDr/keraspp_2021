fn main() {
    println!("Hello, world!");
    
    make_array();
}

fn make_array() {
    let a = [1,2,3,4,5];
    println!("{:?}", a);

    let a: [u32; 5] = [1,2,3,4,5];
    println!("{:?}", a);

    let a = ["Jhon"; 5];
    println!("{:?}", a);
}

// Linked list by Rust
#[derive(Clone)]
enum address {
    address(Box<myList>),
    Nil,
}

#[derive(Clone)]
struct myList {
    value: u32,
    next: address
}

impl myList {
    fn append(&mut self, elem: u32) {
        match self.next {
            address::address(ref mut next_address) => {
                next_address.append(elem);
            }
            address::Nil => {
                let node = myList {
                    value: elem,
                    next: address::Nil,
                };
                self.next = address::address(Box::new(node))
            }
        }
    }

