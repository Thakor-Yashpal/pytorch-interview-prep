import numpy as np
import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor

def pytorh():
    a = np.ones(10)
    b = np.ones(10)* 2
    c = b * a
    d = c + 1
    print(d,c)
    
pytorh()    #pip install torch torchvision torchaudio


# second exapmle

def one():
    A = ("A")
    B = ("B")
    C = A * B
    D = C +(1)
    F = compile (D)
    d = F(A=np.ones(10),B=np.ones(10)*2)

one()  


# Define x as a tensor with gradient tracking enabled
x = pytorch.tensor(1.0, requires_grad=True)

# Define y as a function of x
y = 4 * x + 3

# Perform backward pass to compute the gradient of y w.r.t. x
y.backward()

# Print the gradient of x
print(x.grad)


class TensorCount:
    def __init__(self, count, tensor, cpu_usage, gpu_usage):
        self.count = count
        self.tensor = tensor
        self.cpu_usage = cpu_usage
        self.gpu_usage = gpu_usage
    
    def count_number(self):
        # Generate a random integer tensor
        random_tensor = pytorch.gradient(1, 10, (self.count,), requires_grad=True)
        print("Generated Random Tensor:", random_tensor)

# Create an instance of the class
la_ma = TensorCount(count=5, tensor=None, cpu_usage=50, gpu_usage=75)

# Call the method
la_ma.count_number()



# what is tthe use of torch.from_numpy()

torch.from_numpy() #how to use this function?