# import jax libraries
from jax import numpy as jnp
from jax import grad

# generate data
x = jnp.array([1.0, 2.0, 3.0])
y = jnp.array([3.0, 5.0, 7.0]) # 2.0*x + 1.0

# split data into training and test sets
x_train, y_train, x_test, y_test = x[:2], y[:2], x[2:], y[2:]

# make a model
def f(w, b, x):
    return w*x + b

def J(w, b, x, y):
    return jnp.mean((f(w, b, x) - y)**2)/2

# calculate the gradient of the loss function
dJ_dw = grad(J, argnums=0)
dJ_db = grad(J, argnums=1)

# train the model
w, b = 0.0, 0.0
N_epoch = 1000
learning_rate = 0.1
for epoch in range(N_epoch):
    for x_i, y_i in zip(x_train, y_train):
        dl_dw = dJ_dw(w, b, x_i, y_i)
        dl_db = dJ_db(w, b, x_i, y_i)
        w -= learning_rate * dl_dw
        b -= learning_rate * dl_db
    l = J(w, b, x_train, y_train)
    err = J(w, b, x_test, y_test)
    if epoch % 100 == 0:
        print(f'epoch {epoch} test loss {err:.3e} train loss {l:.3e} w {w:.2f} b {b:.2f}')
