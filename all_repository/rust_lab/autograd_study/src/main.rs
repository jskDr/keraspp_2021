use autograd as ag;

fn main() {
    println!("Hello, world!");

    ag::with(|g: &mut ag::Graph<_>| {
        let x = g.placeholder(&[]);
        let y = g.placeholder(&[]);
        let z = 2.*x*x + 3.*y + 1.;
     
        // dz/dy
        let gy = &g.grad(&[z], &[y])[0];
        println!("{:?}", gy.eval(&[]));   // => Ok(3.)
     
        // dz/dx (requires to fill the placeholder `x`)
        let gx = &g.grad(&[z], &[x])[0];
        let feed = ag::ndarray::arr0(10.);
        println!("{:?}", gx.eval(&[x.given(feed.view())]));  // => Ok(8.)
     
        // ddz/dx (differentiates `z` again)
        let ggx = &g.grad(&[gx], &[x])[0];
        println!("{:?}", ggx.eval(&[]));  // => Ok(4.)
     });
}
