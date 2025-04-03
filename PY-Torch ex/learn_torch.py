import torch 


device = 'cuda' if torch.cuda.is_available() else 'cpu'

print(device)

scaler = torch.tensor(7)
scaler.ndim
scaler.item()
print(scaler.item)
      
vactor = torch.tensor([7,7])
vactor.ndim
vactor.shape   # A tensor with 2 elements cannot be converted to scalar

print(vactor)

matrex = torch.tensor(  [[7,7],
                        [12,12],
                        [14,14]])

print(matrex[1])



# creating a tensor with small data 


# creating a tensor with small data 
  
matrix_data = [[1, 2], [3, 4]]
matrix_tensor = torch.tensor(matrix_data)

print(matrix_tensor)


# creataing a radndom tensor of size (3,4)

random = torch.rand(size= (3,4,5,6))
random,random.dtype
print(random)
print(random.ndim)
print(random.shape)



emty_tensor = []

matrex_tensor = torch.rand(size = (3,244,244))

matrex_tensor,matrex_tensor.ndim,matrex_tensor.ndim

for emty_tensor in matrex_tensor:

    if emty_tensor != matrex_tensor:
        print(f'{"Tis tensor is empty",{emty_tensor}}')
    else:
        print(f'{"This tensor is not empty",{matrex_tensor}}')




# Create a random tensor
matrix_tensor = torch.rand(size=(3, 244, 244))


print(matrix_tensor)



random_imag =torch.rand(size= (3,224,224))
random_imag,random_imag.ndim,random_imag.ndim
print(random_imag)
