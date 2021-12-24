use autograd as ag;

fn main() {
    ag::with(|g: &mut ag::Graph<_>| {
        let x = g.placeholder(&[]);
        let y = (x + 1.)*(x + 1.);
     
        let dy_dx = &g.grad(&[y], &[x])[0];
        let x_val = ag::ndarray::arr0(1.);
        println!("{:?}", dy_dx.eval(&[x.given(x_val.view())])); 
     });
}
