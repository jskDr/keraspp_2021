use pyo3::prelude::*;

#[pymodule]
fn fibonacci(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(fibo, m)?)?;
    Ok(())
}

#[pyfunction]
fn fibo(a: usize) -> PyResult<usize> {
    let r = fibo_calc(a);
    Ok(r)
}

fn fibo_calc(a: usize) -> usize {
    if a < 2 {return a};
    fibo_calc(a-1) + fibo_calc(a-2)
}