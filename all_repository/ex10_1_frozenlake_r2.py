#%%
import gym
flake = gym.make("FrozenLake-v0", is_slippery=False)

#%%
k = 0
new_s = flake.reset()
flake.render()

# %%
import pandas as pd
buff_df = pd.DataFrame({"S":[new_s],"S:(x,y)":[(0,0)], 
            "R":[0.0], "done":[False], 
            "A":[0], "A:name": [""]})
buff_df.index.name = 'k'

Actions = ["Left", "Down", "Right", "Up"]
N_Iter = 3
for iter in range(N_Iter):
    a_k = flake.action_space.sample()
    buff_df.loc[iter,'A':"A:name"] = (a_k, Actions[a_k])
    s, r, done, info = flake.step(a_k)
    flake.render()
    new_df = pd.DataFrame({"S":[s], "S:(x,y)":[(s%4,s//4)],
                            "R":[r], "done":[done], 
                            "A":[0], "A:name": [""]})
    buff_df = buff_df.append(new_df, ignore_index=True)
    buff_df.index.name = 'k'
    if done:
        break
print(buff_df)
# %%
