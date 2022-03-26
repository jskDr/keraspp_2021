

fn find_sum(list:&Vec<f32>) -> f32 {  
    let mut sum:f32 = 0.0;
    for i in 0..list.len() {
        sum += list[i];
    }
    sum
}

fn main() {
    let list:Vec<f32> = 
        vec![10.5, 4.8, 13.2, 6.4, 9.5];
    let sum:f32 = find_sum(&list);

    println!("Sum = {}", sum);
}