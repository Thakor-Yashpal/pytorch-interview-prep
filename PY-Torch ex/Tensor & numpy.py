import torch
import numpy



# Numpy array vs pytorch tensor 

Tensor = torch.tensor([1,2,3], device= 'cpu')

Array = numpy.array([1,2,3])


print (Tensor)

print(Array)