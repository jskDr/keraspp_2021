#%%
import gym
flake = gym.make("FrozenLake-v0", is_slippery=False)

#%%
curr_s = flake.reset()
print(curr_s)
flake.render()

# %%
N_Iter = 3
for iter in range(N_Iter):
    print(f"Iter: {iter}")
    action = flake.action_space.sample()
    print(f"Action --> {action}")
# %%
N_Iter = 3
for iter in range(N_Iter):
    action = flake.action_space.sample()
    new_s, r, done, info = flake.step(action)
    print(f"new_s, r, done, info: {new_s, r, done, info}")
    print("Lake:")
    flake.render()
    if done:
        break
# %%
