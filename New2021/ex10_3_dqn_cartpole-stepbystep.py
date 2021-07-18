# %%
%matplotlib inline

import numpy as np
import random
from collections import deque
import matplotlib.pyplot as plt 
import gym
from keras import Model
from keras.layers import Dense, Input
from keras.optimizers import Adam
import tensorflow as tf

#%%
def create_q_model(num_states, num_actions):
    inputs = Input(shape=num_states)
    layer = Dense(32, activation="relu")(inputs)
    layer = Dense(16, activation="relu")(layer)
    action = Dense(num_actions, activation="linear")(layer)
    return Model(inputs=inputs, outputs=action)

model = create_q_model(4,2)
model.summary()

#%%
def get_env_model():
    env = gym.make('CartPole-v1')
    num_states = env.observation_space.shape[0]
    num_actions = env.action_space.n
    model = create_q_model(num_states, num_actions)
    return env, model

env, model = get_env_model()
env.reset()
env.render()
#%%
env.close()

#%%
def train(model):
    state_size = 4
    action_size = 2        
    # model = DQN(action_size)
    states = np.zeros((10,state_size))
    with tf.GradientTape() as tape:
        predicts = model(states)
    print('Completed!')



env, model = get_env_model()
train(model)

# %%
class World_00:
    def __init__(self):
        self.get_env_model()

    def get_env_model(self):
        self.env = gym.make('CartPole-v1')
        self.num_states = env.observation_space.shape[0]
        self.num_actions = env.action_space.n
        self.model = create_q_model(self.num_states, self.num_actions)
        # print(self.model.summary())

    def train(self):        
        states = np.zeros((10,self.num_states))
        with tf.GradientTape() as tape:
            predicts = self.model(states)
        print('Completed!')

new_world = World_00()
new_world.train()

# %%
def env_test_model_memory(memory, env, model, n_episodes=1000, 
        flag_render=False):
    for e in range(n_episodes):
        done = False
        score = 0
        s = env.reset()
        while not done:
            s_array = np.array(s).reshape((1,-1))
            Qsa = model.predict(s_array)[0]
            a = np.argmax(Qsa)
            next_s, r, done, _ = env.step(a)
            if flag_render:
                env.render()
            score += r
            memory.append([s,a,r,next_s,done])
        print(f'Episode: {e:5d} -->  Score: {score:3.1f}')
    print('Notice that the max score is set to 500.0 in CartPole-v1')

def list_rotate(l):
    return list(zip(*l))

class World_01(World_00):
    def __init__(self):
        World_00.__init__(self)
        self.memory = deque(maxlen=2000)
        self.N_batch = 64
        self.t_model = create_q_model(self.num_states, self.num_actions)
        self.discount_factor = 0.99
        self.learning_rate = 0.001
        self.optimizer = Adam(lr=self.learning_rate)

    def trial(self, flag_render=False):
        env_test_model_memory(self.memory, self.env,
            self.model, n_episodes=10, flag_render=flag_render)
        print(len(self.memory))

    def train_memory(self):
        if len(self.memory) >= self.N_batch:
            memory_batch = random.sample(self.memory, self.N_batch)
            s_l,a_l,r_l,next_s_l,done_l = [np.array(x) for x in list_rotate(memory_batch)]
            model_w = self.model.trainable_variables
            with tf.GradientTape() as tape:
                Qsa_pred_l = self.model(s_l)
                a_l_onehot = tf.one_hot(a_l, self.num_actions)
                Qs_a_pred_l = tf.reduce_sum(a_l_onehot * Qsa_pred_l, axis=1)    

                Qsa_tpred_l = self.t_model(next_s_l) 
                Qsa_tpred_l = tf.stop_gradient(Qsa_tpred_l)

                max_Q_next_s_a_l = np.amax(Qsa_tpred_l, axis=-1)
                Qs_a_l = r_l + (1 - done_l) * self.discount_factor * max_Q_next_s_a_l
                loss = tf.reduce_mean(tf.square(Qs_a_l - Qs_a_pred_l))
            grads = tape.gradient(loss, model_w)
            self.optimizer.apply_gradients(zip(grads, model_w))

new_world = World_01()
new_world.trial(flag_render=True)
new_world.train_memory()
new_world.env.close()
print('Completed!')

# %%
class World_02(World_01):
    def __init__(self):
        World_01.__init__(self)
        self.epsilon = 0.2
    
    def update_t_model(self):
        self.t_model.set_weights(self.model.get_weights())

    def best_action(self, s):
        if random.random() <= self.epsilon:
            return random.randrange(self.num_actions)
        else:
            s_array = np.array(s).reshape((1,-1))
            Qsa = self.model.predict(s_array)[0]
            return np.argmax(Qsa)

    def trials(self, n_episodes=100, flag_render=False):
        memory = self.memory
        env = self.env
        model = self.model        
        for e in range(n_episodes):
            done = False
            score = 0
            s = env.reset()
            while not done:                
                a = self.best_action(s)
                next_s, r, done, _ = env.step(a)
                if flag_render:
                    env.render()
                score += r
                memory.append([s,a,r,next_s,done])
                # self.train_memory()     
                s = next_s
                self.train_memory()                 
            self.update_t_model()
            print(f'Episode: {e:5d} -->  Score: {score:3.1f}')   

new_world = World_02()
new_world.trials(n_episodes=100)
new_world.env.close()
print('Completed!')