# %% 
import torch
x = torch.tensor(5.0)
print(x)
# %%
x.requires_grad_()
y = x**2
y.backward()
x.grad