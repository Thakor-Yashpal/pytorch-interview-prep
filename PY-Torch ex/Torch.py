import torch
import numpy as np


device = 'cuda' if torch.cuda.is_available() else 'cpu'

print(device)
# how to work with tensor?

# list = [[1,2,3,4,5,6],[1,2,3,4,5,6]]

# print(list)

# tensor = torch.tensor(list)

# print(tensor)



# Numpy Array 

np1 =np.random.rand(3,4)

print(np1)



# ------ how to createa tensor -----

tensor_2d =torch.randn(3,4)

print(tensor_2d)


