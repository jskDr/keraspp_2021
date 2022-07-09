#%% importing libraries
from jax import grad, random
from jax import numpy as jnp

#%% preparing data
x = jnp.array([1.0, 2.0, 3.0])
y = 2.0*x + 1.0

# split train and test data
N = 2
x_train, y_train, x_test, y_test = x[:N], y[:N], x[N:], y[N:]
print(x_train, y_train, x_test, y_test)

#%% define the model
def model(w, b, x):
    return w*x + b

def loss(w, b, x, y):
    y_hat = model(w, b, x)
    return jnp.mean((y_hat - y)**2)

dloss_dw = grad(loss, argnums=0)
dloss_db = grad(loss, argnums=1)

#%% train model
w, b = 0.0, 0.0
N_epoch = 100
for epoch in range(N_epoch):
    for x_i, y_i in zip(x_train, y_train):
        dl_dw = dloss_dw(w, b, x_i, y_i)
        dl_db = dloss_db(w, b, x_i, y_i)
        w -= 0.01 * dl_dw
        b -= 0.01 * dl_db
    l = loss(w, b, x_train, y_train)
    err = loss(w, b, x_test, y_test)
    if epoch % 10 == 0:
        print(f'epoch {epoch}: test loss {err:.3e}, train loss {l:.3e}, w {w:.2f}, b {b:.2f}')
# %%
