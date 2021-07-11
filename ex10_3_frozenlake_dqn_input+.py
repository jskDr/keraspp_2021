# %%
"""
NN에서 입력을 이진으로 만든다. tf.one_hot(indices, depth, ...) 활용 
""" 
%matplotlib inline

import gym
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

flake = gym.make("FrozenLake-v0", is_slippery=False)
flake.render()
Q = np.zeros((flake.observation_space.n, flake.action_space.n))
PI = np.argmax(Q,axis=1)

# %% Create model
import keras 
from keras.layers import Input, Dense
from keras import Model

# %%
def create_q_model(num_states, num_actions):
    inputs = Input(shape=num_states)
    #layer = Dense(32, activation="relu")(inputs)
    #layer = Dense(16, activation="relu")(layer)
    #layer = Dense(1, activation="relu")(inputs)
    layer = inputs
    action = Dense(num_actions, activation="linear")(layer)
    return keras.Model(inputs=inputs, outputs=action)

model = create_q_model(flake.observation_space.n, flake.action_space.n)
print(model.summary())
print('Show intial model weights:')
print(model.get_weights())

# %% Predit Q(s,a) for given s
import tensorflow as tf
s = 0
s_array = np.array([s])
s_array_onehot = tf.one_hot(s_array, depth=flake.observation_space.n)
a_array = model.predict(s_array_onehot)
a = np.argmax(a_array)
print(f"One-hot state:{s_array} --> {s_array_onehot}")
print(f"Q(s,a)|s=0 for all a -> {a_array}")
print(f"Best action: max_a Q(s,a)|s=0 = {a}")

# %% Calculate the best policy for the given Q(s,a)
all_states = np.arange(flake.observation_space.n)
all_states_onehot = tf.one_hot(all_states,
    depth=flake.observation_space.n)
Q_all = model.predict(all_states_onehot)
PI = np.argmax(Q_all, axis=1)
print("All states:", all_states)
print("All states in one-hot form:")
print(all_states_onehot)
print("Q[s,a] for all s,a:")
print(Q_all)
print(f"PI[s] for all s: {PI}")

# %% define optimizer, loss_fn and makes model copy
optimizer = keras.optimizers.Adam(learning_rate=0.00025, clipnorm=1.0)
#loss_fn = keras.losses.Huber()
loss_fn = keras.losses.MeanSquaredError()
# make a model which copies the same weight from model after some delay
model_target = create_q_model(flake.observation_space.n, 
    flake.action_space.n)

# %% load optimal Q(s,a)
print('Optial Q(s,a) is loaded:') 
#print(Q_opt)

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

    Actions = ["0:Left", "1:Down", "2:Right", "3:Up"]
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
S_array = buff_df.S.to_numpy()
A_array = buff_df.A.to_numpy()
S_tensor = tf.convert_to_tensor(S_array)
A_tensor = tf.convert_to_tensor(A_array)

# Qs_tensor = model.predict(S_tensor)
S_tensor_onehot = tf.one_hot(S_tensor, flake.observation_space.n)
Qs_tensor = model(S_tensor_onehot)
A_masks = tf.one_hot(A_tensor, flake.action_space.n)
Qsa_tensor = tf.reduce_sum(tf.multiply(Qs_tensor, A_masks), axis=1)

print(f"S_tensor: {S_tensor}")
print(f"A_tensor: {A_tensor}")
print("Qs_tensor:")
print(Qs_tensor)
print(f"A_masks: {A_masks}")
print("Qsa_tensor:")
print(Qsa_tensor)

# %% evaluate loss and qnn_update
def qnn_update(buff_df, model, model_target, loss_fn, 
        optimizer, learning_rate=0.01,
        disp_flag=False):
    R_array = buff_df.R.to_numpy()
    if disp_flag:
        print(f"R_array: {R_array}")

    S_next_array = np.append(buff_df.S.to_numpy()[1:], 0)
    S_next_tensor = tf.convert_to_tensor(S_next_array)
    S_next_tensor_onehot = tf.one_hot(S_next_tensor, 
        flake.observation_space.n)
    Qs_next_tensor = model_target.predict(S_next_tensor_onehot)
    Qsa_next_max_tensor = tf.reduce_max(Qs_next_tensor, axis=1)
    Qsa_update = R_array + learning_rate * Qsa_next_max_tensor 
    if disp_flag:
        print(f"Qsa_update: {Qsa_update}")

    S_array = buff_df.S.to_numpy()
    A_array = buff_df.A.to_numpy()
    S_tensor = tf.convert_to_tensor(S_array)
    A_tensor = tf.convert_to_tensor(A_array)
    with tf.GradientTape() as tape:
        S_tensor_onehot = tf.one_hot(S_tensor, flake.observation_space.n)
        Qs_tensor = model(S_tensor_onehot)
        A_masks = tf.one_hot(A_tensor, flake.action_space.n)
        Qsa_tensor = tf.reduce_sum(tf.multiply(Qs_tensor, A_masks), axis=1)
        loss = loss_fn(Qsa_update, Qsa_tensor)
        if disp_flag:
            print(f"loss: {loss}")

    grads = tape.gradient(loss, model.trainable_variables)
    optimizer.apply_gradients(zip(grads, model.trainable_variables))

# Q_all = model(np.arange(flake.observation_space.n)) --> onehot version
all_states = np.arange(flake.observation_space.n)
all_states_onehot = tf.one_hot(all_states,
    depth=flake.observation_space.n)
Q_all = model.predict(all_states_onehot)
PI = np.argmax(Q_all, axis=1)
buff_df = run_with_PI_exploration(PI, exploration=0.8, N_Iter=100)
qnn_update(buff_df, model, model_target, loss_fn, 
        optimizer, learning_rate=0.01, disp_flag=True)

# %%
def model_onehot(inputs, depth):
    inputs_onehot = tf.one_hot(input, depth)
    return model.predict(all_states_onehot)       

def q_learning_nn(
        model, model_target, loss_fn, optimizer,
        N_epoch=1000, N_Iter=100, learning_rate=0.01, exploration=0.2, 
        trace_flag=False,
        display_period=10):
    """
    return PI 1-D integer array if trace_flag is False 
    else return PI_array 2-D integer array 
    """
    PI_list = []
    for e in range(N_epoch):
        # Q_all = model(np.arange(flake.observation_space.n))
        all_states = np.arange(flake.observation_space.n)
        all_states_onehot = tf.one_hot(all_states,
            depth=flake.observation_space.n)
        Q_all = model.predict(all_states_onehot)        
        PI = np.argmax(Q_all, axis=1)
        buff_df = run_with_PI_exploration(PI, exploration=exploration, 
                        N_Iter=N_Iter)
        qnn_update(buff_df, model, model_target, loss_fn, 
            optimizer, learning_rate=0.01)

        # 아래는 매번이 아니고 주기적으로 복사가 되어야 성능 개선이 가능함  
        if e % 10 == 0:
            model_target.set_weights(model.get_weights()) 

        PI_list.append(PI)
        if display_period > 0 and (e+1) % display_period == 0:
            print(f"Epoch + 1: PI = {e+1}: {PI}")
    if trace_flag:
        return np.array(PI_list)
    else:
        return PI

PI_array = q_learning_nn(
                model, model_target, loss_fn, optimizer,
                N_epoch=2000, N_Iter=100, learning_rate=0.1, 
                exploration=0.2, trace_flag=True)
               
print(PI_array)
plt.plot(PI_array)
flake.render()
print(PI_array[-1].reshape(4,4))
print(["Left", "Down", "Right", "Up"])
# %%
