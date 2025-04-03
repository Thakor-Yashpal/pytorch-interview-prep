import torch
import numpy
import numpy as np 


# Numpy array vs pytorch tensor 

# Tensor = torch.tensor([1,2,3], device= 'cpu')

# Array = numpy.array([1,2,3])


# print (Tensor)

# print(Array)


#------------ numpy array for createing random numbers for tesnsor ----------



# --------Tesnsor 2d and 3d,how to createa tensor------------

# tensor_2d =torch.randn(3,4)

# print(tensor_2d)

# tensor_3d =torch.zeros(2,3,4)

# print(tensor_3d)


# createa tensor out of numpy array

np1 =np.random.rand(3,4)

VL01 = torch.from_numpy(np1)
print(VL01)

