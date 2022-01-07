# %%
import tensorflow as tf

def df(x):
    with tf.GradientTape() as t:
        t.watch(x)
        # y = x**2
        y = tf.sin(x)
    return t.gradient(y, x)

# %%
x = tf.Variable(5.0)
dy = df(x)
print(dy)

# %% jax
from jax import grad
x = 5.0
y = lambda x: x**2
dy = grad(y)
# %%
dy(5.0)
# %%

@tf.function
def fn_tf(x):
    return tf.sin(x)

fn_tf(2.0)

# %%
