# %%
import gym
flake = gym.make("FrozenLake-v0", is_slippery=False)

# %%
new_s = flake.reset()
flake.render()

# %%
for _ in range(3):
        a_k = flake.action_space.sample()
        s, r, done, info = flake.step(a_k)
        flake.render()
        if done:
            break

# %%
import pandas as pd

def run(N_Iter = 100, render_flag=False):
    """
    Return buff_df if done, otherwise return None 
    """
    new_s = flake.reset()
    if render_flag: flake.render()
    buff_df = pd.DataFrame({"S":[new_s],"S:(x,y)":[(0,0)], 
                "R":[0.0], "done":[False], 
                "A":[0], "A:name": [""]})
    buff_df.index.name = 'k'

    Actions = ["Left", "Down", "Right", "Up"]
    for iter in range(N_Iter):
        a_k = flake.action_space.sample()
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

run(10)

# %%
import numpy as np
def calc_g(r, factor = 0.9):
    # r = buff_df.R.values
    g_prev = 0
    g = np.copy(r)
    for rev_k in range(len(g)-1,-1,-1):
        g[rev_k] += factor * g_prev
        g_prev = g[rev_k]
    # buff_df['G'] = g
    return g

buff_df = run(10)
if buff_df is not None:
    r = buff_df.R.values
    buff_df['G'] = calc_g(r)
else:
    print('Try more iterations for each run')
buff_df
# %%
