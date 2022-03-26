
fn binary_search(a:&Vec<isize>, 
    l:usize, h:usize, x:isize)->isize{
    let m:usize = (l+h)/2;
    if l <= h {
        if a[m]==x {
            return m as isize;
        }
        else if a[m] > x {
            return binary_search(a,l,m-1,x);
        }
        else {
            return binary_search(a,m+1,h,x);
        }
    }
    -1
}

fn main() {
    let arr = vec![ 2, 3, 4, 10, 40];
    let x = 10;
    let result:isize;

    result = binary_search(&arr, 0, arr.len(), x); 

    println!("{}", result);
}        