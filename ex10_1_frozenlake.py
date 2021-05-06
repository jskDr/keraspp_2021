#%%
import gym
flake = gym.make("FrozenLake-v0", is_slippery=False)

#%%
k = 0
new_s = flake.reset()
flake.render()

# %%
Actions = ["Left", "Down", "RIght", "Up"]
N_Iter = 2
for iter in range(N_Iter):
    a = flake.action_space.sample()
    curr_s = new_s
    print()
    print(f"S[{k}] = {curr_s} : (x,y)=({new_s%4},{new_s//4})")
    print(f"A[{k}] = {a} : {Actions[a]}")
    new_s, r, done, info = flake.step(a)
    k = k + 1
    print(f"S[{k}] = {new_s} : (x,y)=({new_s%4},{new_s//4})")
    print(f"R[{k}] = {r}")
    print(f"Done = {done}")
    flake.render()
    if done:
        break
# %%
