import torch 

<<<<<<< Updated upstream
# scaler = torch.tensor(7)
# scaler.ndim
# scaler.item()
# print(scaler.item())
=======
# #  
>>>>>>> Stashed changes

# matrex = torch.tensor(  [[7,7],
#                         [12,12],
#                         [14,14]])

# print(matrex[1])


<<<<<<< Updated upstream
# creating a tensor with small data 

=======
# # creating a tensor with small data 
  
# matrix_data = [[1, 2], [3, 4]]
# matrix_tensor = torch.tensor(matrix_data)
# print(matrix_tensor)


# creataing a radndom tensor of size (3,4)

# random = torch.rand(size= (3,4,5,6))
# random,random.dtype
# print(random)
# print(random.ndim)
# print(random.shape)


# random_imag =torch.rand(size= (3,224,224))
# random_imag,random_imag.ndim,random_imag.ndim
# print(random_imag)

emty_tensor = []

matrex_tensor = torch.rand(size = (3,244,244))

matrex_tensor,matrex_tensor.ndim,matrex_tensor.ndim

for emty_tensor in matrex_tensor:

    if emty_tensor != matrex_tensor:
        print(f'{"Tis tensor is empty",{emty_tensor}}')
    else:
        print(f'{"This tensor is not empty",{matrex_tensor}}')




# # Create a random tensor
# matrix_tensor = torch.rand(size=(3, 244, 244))

# # Iterate through the rows of the tensor
# for row in matrix_tensor:
#     # Check if all elements in the row are zero.
#     if torch.all(row == 0):  # Use torch.all for element-wise comparison
#         print("This row is empty (all zeros).")
#     else:
#         print("This row is not empty (contains non-zero elements).")
>>>>>>> Stashed changes
