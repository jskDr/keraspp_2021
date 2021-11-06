
/*
Compile by:
$ maturin develop

Notice that it is compatible with both python list and array for input argument. 
How to return as numpy array is the question now. 
*/
use pyo3::prelude::*;
// use std::convert::TryFrom;

/// Formats the sum of two numbers as string.
#[pyfunction]
fn sum_as_string(a: usize, b: usize) -> PyResult<String> {
    Ok((a + b).to_string())
}

#[pyfunction]
fn sum_as_int(a: usize, b: usize) -> PyResult<usize> {
    Ok(a + b)
}

#[pyfunction]
fn multiply_as_int(a: usize, b: usize) -> PyResult<usize> {
    Ok(a * b)
}

#[pyfunction] // make a new function within a new library with pyfunction macro
fn sum_for_usize(y: Vec<usize>) -> PyResult<usize> {
    // let x = x.into_iter().map(TryFrom::try_from).collect::<Result<Vec<_>, _>>();
    // let y = y.into_iter().map(TryFrom::try_from).collect::<Result<Vec<_>, _>>();
    // Error handling is missing here, you'll need to look into PyO3's documentation for that
    //
    // return original lib's function return
    let mut z = 0;
    for y_each in y.iter() {
        z += y_each;
    }
    Ok(z)
}

#[pyfunction] // make a new function within a new library with pyfunction macro
fn add_scalar_for_usize(y: Vec<usize>, a: usize) -> PyResult<Vec<usize>> {
    let mut z = y.clone();
    for (i, y_each) in y.iter().enumerate() {
        z[i] = y_each + a;
    }
    Ok(z)
}


/// A Python module implemented in Rust. The name of this function must match
/// the `lib.name` setting in the `Cargo.toml`, else Python will not be able to
/// import the module.
#[pymodule]
fn string_sum(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(sum_as_string, m)?)?;
    m.add_function(wrap_pyfunction!(sum_as_int, m)?)?;
    m.add_function(wrap_pyfunction!(multiply_as_int, m)?)?;
    m.add_function(wrap_pyfunction!(sum_for_usize, m)?)?;
    m.add_function(wrap_pyfunction!(add_scalar_for_usize, m)?)?;

    Ok(())
}