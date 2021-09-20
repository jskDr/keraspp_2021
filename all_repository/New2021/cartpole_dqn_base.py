# %% import associated packages
# %matplotlib inline

import gym
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random 

test_flag = True

# %% Environment Open and Render
def env_test_random(env, n_episodes=1000):
    for e in range(n_episodes):
        done = False
        score = 0
        s = env.reset()
        while not done:
            a = random.randrange(env.action_space.n)
            next_s, r, done, _ = env.step(a)
            env.render()
            score += r
        print(f'Episode: {e:5d} -->  Score: {score:3.1f}')
    print('Notice that the max score is set to 500.0 in CartPole-v1')

if test_flag:
    env = gym.make('CartPole-v1')
    env_test_random(env, n_episodes=200)
    env.close()

# %% NN Model for Q(s,a)
import tensorflow as tf
from tensorflow import keras 
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras import Model 

def create_q_model(num_states, num_actions):
    inputs = Input(shape=num_states)
    layer = Dense(32, activation="relu")(inputs)
    layer = Dense(16, activation="relu")(layer)
    action = Dense(num_actions, activation="linear")(layer)
    return Model(inputs=inputs, outputs=action)

def get_env_model():
    env = gym.make('CartPole-v1')
    num_states = env.observation_space.shape[0]
    num_actions = env.action_space.n
    model = create_q_model(num_states, num_actions)
    print(model.summary())
    return env, model

if test_flag:
    env, model = get_env_model()

    s = env.reset()
    print(s)
    s_batch = s.reshape(1,-1)
    print(s_batch)
    Qs_a = model.predict(s_batch)[0]
    print(f'Qsa|s=s0: {Qs_a}')
    a = np.argmax(model.predict(s_batch)[0])
    print(f'Best action: {a}')

# %% action predicted by NN
def env_test_model(env, model, n_episodes=1000):
    for e in range(n_episodes):
        done = False
        score = 0
        s = env.reset()
        while not done:
            s_array = np.array(s).reshape((1,-1))
            Qsa = model.predict(s_array)[0]
            a = np.argmax(Qsa)
            next_s, r, done, _ = env.step(a)
            env.render()
            score += r
        print(f'Episode: {e:5d} -->  Score: {score:3.1f}')
    print('Notice that the max score is set to 500.0 in CartPole-v1')

if test_flag:
    env, model = get_env_model()
    env_test_model(env, model, n_episodes=10)
    env.close()

# %% Memory for history
def env_test_model_memory(memory, env, model, n_episodes=1000):
    for e in range(n_episodes):
        done = False
        score = 0
        s = env.reset()
        while not done:
            s_array = np.array(s).reshape((1,-1))
            Qsa = model.predict(s_array)[0]
            a = np.argmax(Qsa)
            next_s, r, done, _ = env.step(a)
            env.render()
            score += r
            memory.append([s,a,r,next_s,done])
        print(f'Episode: {e:5d} -->  Score: {score:3.1f}')
    print('Notice that the max score is set to 500.0 in CartPole-v1')

if test_flag:
    env, model = get_env_model()
    memory = []
    env_test_model_memory(memory, env, model, n_episodes=10)
    print(f'Length of memory: {len(memory)}')
    print('memory[0] = [s,a,r,next_s,done]:')
    print(memory[0])
    env.close()

# %%
def list_rotate(l):
    return list(zip(*l))

N_batch = 10
env, model = get_env_model()
memory = []
env_test_model_memory(memory, env, model, n_episodes=10)
if len(memory) > N_batch:
    print(len(memory))
    memory_batch = random.sample(memory, N_batch)
    print(len(memory_batch))
    s_l,a_l,r_l,next_s_l,done_l = list_rotate(memory_batch)
    print(f'a_l: {a_l}')
env.close()

# %%
from tensorflow.keras.initializers import RandomUniform
class DQN(tf.keras.Model):
    def __init__(self, action_size):
        super(DQN, self).__init__()
        self.fc1 = Dense(24, activation='relu')
        self.fc2 = Dense(24, activation='relu')
        self.fc_out = Dense(action_size,
                            kernel_initializer=RandomUniform(-1e-3, 1e-3))

    def call(self, x):
        x = self.fc1(x)
        x = self.fc2(x)
        q = self.fc_out(x)
        return q

N_batch = 10
env, model = get_env_model()
model = DQN(env.action_space.n)
memory = []
env_test_model_memory(memory, env, model, n_episodes=10)
if len(memory) > N_batch:
    mini_batch = random.sample(memory, N_batch)
    states = np.array([sample[0] for sample in mini_batch])
    actions = np.array([sample[1] for sample in mini_batch])
    rewards = np.array([sample[2] for sample in mini_batch])
    next_states = np.array([sample[3] for sample in mini_batch])
    dones = np.array([sample[4] for sample in mini_batch])
    # s_l,a_l,r_l,next_s_l,done_l = [np.array(x) for x in list_rotate(memory_batch)]
    with tf.GradientTape() as tape:
        Qsa_preds = model.predict(states)
    print(Qsa_pred)

env.close()
# %%
env.close()
# %%
