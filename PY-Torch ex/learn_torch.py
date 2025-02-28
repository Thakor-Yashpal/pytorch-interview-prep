import torch 

scaler = torch.tensor(7)
scaler.ndim
scaler.item()
print(scaler.item())

vactor = torch.tensor([7,7])
vactor.ndim
vactor.shape   # A tensor with 2 elements cannot be converted to scalar

print(vactor)

matrex = torch.tensor(  [[7,7],
                        [12,12],
                        [14,14]])

print(matrex[1])


# creating a tensor with small data 
  
matrix_data = [[1, 2], [3, 4]]
matrix_tensor = torch.tensor(matrix_data)
print(matrix_tensor)