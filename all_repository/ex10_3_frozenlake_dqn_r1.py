# %% 
import gym
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

flake = gym.make("FrozenLake-v0", is_slippery=False)
Q = np.zeros((flake.observation_space.n, flake.action_space.n))
PI = np.argmax(Q,axis=1)

# %% Create model
import keras 
from keras.layers import Input, Dense
from keras import Model

# %%
def create_q_model(shape_states, num_actions):
    inputs = Input(shape=(1,)+shape_states)
    layer1 = Dense(16, activation="relu")(inputs)
    layer2 = Dense(16, activation="relu")(layer1)
    action = Dense(num_actions, activation="linear")(layer2)
    return keras.Model(inputs=inputs, outputs=action)

model = create_q_model(flake.observation_space.shape, flake.action_space.n)
print(model.summary())

# %% Predit Q(s,a) for given s
s = 0
s_array = np.array([s])
a_array = model.predict(s_array)
a = np.argmax(a_array)
print(f"Q(s,a)|s=0 for all a -> {a_array}")
print(f"Best action: max_a Q(s,a)|s=0 = {a}")

# %% Calculate the best policy for the given Q(s,a)
Q_all = model.predict(np.arange(flake.observation_space.n))
PI = np.argmax(Q_all, axis=1)
print(f"PI[s] for all s: {PI}")

# %% Q-learning
def run_with_PI_exploration(PI=None, exploration=0.2, N_Iter = 100, 
        render_flag=False):
    """
    Return buff_df if done, otherwise return None 
    """
    if PI is None:
        # No PI, action will be determined fully randomly
        exploration = 1.0

    s = flake.reset()
    if render_flag: flake.render()
    buff_df = pd.DataFrame({"S":[s],"S:(x,y)":[(0,0)], 
                "R":[0.0], "done":[False], 
                "A":[0], "A:name": [""]})
    buff_df.index.name = 'k'

    Actions = ["Left", "Down", "Right", "Up"]
    rand_buff =  np.random.rand(N_Iter)
    for iter in range(N_Iter):
        # if np.random.rand() <= exploration:
        if rand_buff[iter] <= exploration:
            a_k = flake.action_space.sample()
        else:
            a_k = PI[s]
        buff_df.loc[iter,'A':"A:name"] = (a_k, Actions[a_k])
        s, r, done, info = flake.step(a_k)
        if render_flag: flake.render()
        new_df = pd.DataFrame({"S":[s], "S:(x,y)":[(s%4,s//4)],
                                "R":[r], "done":[done], 
                                "A":[0], "A:name": [""]})
        buff_df = buff_df.append(new_df, ignore_index=True)
        buff_df.index.name = 'k'
        if done:
            return buff_df
    return None

buff_df = run_with_PI_exploration(PI, exploration=0.8, N_Iter=100)
buff_df

# %% array to tensor and predict Q by tensor
import tensorflow as tf

S_array = buff_df.S.to_numpy()
A_array = buff_df.A.to_numpy()
S_tensor = tf.convert_to_tensor(S_array)
A_tensor = tf.convert_to_tensor(A_array)

# Qs_tensor = model.predict(S_tensor)
Qs_tensor = model(S_tensor)
A_masks = tf.one_hot(A_tensor, flake.action_space.n)
Qsa_tensor = tf.reduce_sum(tf.multiply(Qs_tensor, A_masks), axis=1)

print(f"S_tensor: {S_tensor}")
print(f"A_tensor: {A_tensor}")
print("Qs_tensor:")
print(Qs_tensor)
print(f"A_masks: {A_masks}")
print("Qsa_tensor:")
print(Qsa_tensor)

# %% define optimizer, loss_fn and makes model copy
optimizer = keras.optimizers.Adam(learning_rate=0.00025, clipnorm=1.0)
loss_fn = keras.losses.Huber()
# make a model which copies the same weight from model after some delay
model_target = create_q_model(flake.observation_space.shape, 
    flake.action_space.n)

# %% evaluate loss and qnn_update
def qnn_update(buff_df, model, model_target, loss_fn, 
        optimizer, learning_rate=0.01):
    #updated_q_values = rewards_sample + gamma * tf.reduce_max(
    #    future_rewards, axis=1)
    R_array = buff_df.R.to_numpy()
    print(f"R_array: {R_array}")

    S_next_array = np.append(buff_df.S.to_numpy()[1:], 0)
    S_next_tensor = tf.convert_to_tensor(S_next_array)
    Qs_next_tensor = model_target.predict(S_next_tensor)
    Qsa_next_max_tensor = tf.reduce_max(Qs_next_tensor, axis=1)
    Qsa_update = R_array + learning_rate * Qsa_next_max_tensor 
    print(f"Qsa_update: {Qsa_update}")

    S_array = buff_df.S.to_numpy()
    A_array = buff_df.A.to_numpy()
    S_tensor = tf.convert_to_tensor(S_array)
    A_tensor = tf.convert_to_tensor(A_array)
    with tf.GradientTape() as tape:
        Qs_tensor = model(S_tensor)
        A_masks = tf.one_hot(A_tensor, flake.action_space.n)
        Qsa_tensor = tf.reduce_sum(tf.multiply(Qs_tensor, A_masks), axis=1)
        loss = loss_fn(Qsa_update, Qsa_tensor)
        print(f"loss: {loss}")

    grads = tape.gradient(loss, model.trainable_variables)
    optimizer.apply_gradients(zip(grads, model.trainable_variables))

Q_all = model(np.arange(flake.observation_space.n))
PI = np.argmax(Q_all, axis=1)
buff_df = run_with_PI_exploration(PI, exploration=0.8, N_Iter=100)
qnn_update(buff_df, model, model_target, loss_fn, 
        optimizer, learning_rate=0.01)
# %%
def q_learning_nn(N_epoch=1000, N_Iter=100, learning_rate=0.01, exploration=0.2, 
        trace_flag=False):
    """
    return PI 1-D integer array if trace_flag is False 
    else return PI_array 2-D integer array 
    """
    PI_list = []
    for e in range(N_epoch):
        Q_all = model(np.arange(flake.observation_space.n))
        PI = np.argmax(Q_all, axis=1)
        buff_df = run_with_PI_exploration(PI, exploration=0.8, N_Iter=100)
        qnn_update(buff_df, model, model_target, loss_fn, 
            optimizer, learning_rate=0.01)
        PI_list.append(PI)
    if trace_flag:
        return np.array(PI_list)
    else:
        return PI

PI_array = q_learning(N_epoch=1000, N_Iter=100, learning_rate=0.01, exploration=0.8, trace_flag=True)
print(PI_array)
plt.plot(PI_array)