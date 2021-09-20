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
    g_prev = 0
    g = np.copy(r[1:])
    g = np.append(g, 0.0) # g[-1] is fixed to 0.0
    for rev_k in range(len(g)-2,-1,-1): 
        g[rev_k] += factor * g_prev
        g_prev = g[rev_k]
    return g

buff_df = run(100)    
calc_g(buff_df.R.values)

# %%
def get_g(N_Iter=50):
    buff_df = run(N_Iter)
    if buff_df is not None:
        r = buff_df.R.values
        buff_df['G'] = calc_g(r)
    else:
        print('Try more iterations for each run')
        return None
    return buff_df

get_g()

# %%
def get_g_many(N_Epochs=5, N_Iter=50):
    gbuff_df = None
    for epoch in range(N_Epochs):
        buff_df = get_g(N_Iter) 
        if buff_df is not None:
            if epoch == 0:
                gbuff_df = buff_df
            else:
                gbuff_df = gbuff_df.append(buff_df)
    return gbuff_df

get_g_many()

# %%
# Calculate V[s]
gbuff_df = get_g_many(100)
V = np.zeros(flake.observation_space.n)
# N_V[S]: no of G values to calculate V[S]
N_V = np.zeros(flake.observation_space.n) 
for s in range(flake.observation_space.n):
    Gs_all = gbuff_df.G[gbuff_df.S==s].values
    if len(Gs_all) > 0:
        V[s] = np.average(Gs_all)
        N_V[s] = len(Gs_all)

V_df = pd.DataFrame({"V": V, "No of Gs": N_V})
V_df.index.name = 's'
V_df

# %% 
# Calculate Q[s,a]
gbuff_df = get_g_many(10)
Q = np.zeros((flake.observation_space.n, flake.action_space.n))
# N_Q[s,a]: no of G values to calculate Q[s,a]
N_Q = np.zeros((flake.observation_space.n, flake.action_space.n)) 
S_list = []
A_list = []
for s in range(flake.observation_space.n):
    for a in range(flake.action_space.n):
        Gs_all = gbuff_df.G[(gbuff_df.S==s) & (gbuff_df.A==a)].values
        if len(Gs_all) > 0:
            Q[s,a] = np.average(Gs_all)
            N_Q[s,a] = len(Gs_all)
        S_list.append(s)
        A_list.append(a)
Q, N_Q, S_list, A_list
SA_df = pd.DataFrame({"S": S_list, "A": A_list})
#Q_df = pd.DataFrame({"S": S_list, "A": A_list, 
#            "Q": Q.reshape(-1), "No of Gs": N_Q.reshape(-1)})
Q_df = pd.DataFrame({"Q": Q.reshape(-1), "No of Gs": N_Q.reshape(-1)},
                    index=pd.MultiIndex.from_frame(SA_df))
Q_df
