#[derive(Clone)]
enum Address {
    Address(Box<ListNode>),
    Nil,
}

#[derive(Clone)]
struct ListNode {
    data: u32,
    next: Address,
}

impl ListNode {
    fn append(&mut self, elem: u32) {
        match self.next {
            Address::Address(ref mut next_address) => {
                next_address.append(elem);
            }
            Address::Nil => {
                let node = ListNode {
                    data: elem,
                    next: Address::Nil,
                };
                self.next = Address::Address(Box::new(node));
            }
        }
    }
    fn list(&self) {
        if self.data == 0 {
            println!("The list is empty.")
        } else {
            println!("{}", self.data);
            match self.next {
                Address::Address(ref next_address) => {
                    next_address.list();
                }
                Address::Nil => {}
            }
        }
    } 
}

fn main() {
    println!("Hello Rust");

    let mut a: [i32; 10] = [0; 10];
    // let mut a: [i32; 10]; (Not allowed)
    a[5] =  37;

    println!("a[5] = {}", a[5]);

    let mut node = ListNode {
        data: 37,
        next: Address::Nil,
    };
    println!("node.data = {}", node.data);

    node.append(3);
    node.list();
}