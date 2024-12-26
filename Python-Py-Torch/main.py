import numpy as np 
import torch as py

# def pytorh():
#     a = np.ones(10)
#     b = np.ones(10)* 2
#     c = b * a
#     d = c + 1
#     print(d,c)

# pytorh()    


# second exapmle
def one():
    A = ("A")
    B = ("B")
    C = A * B
    D = C +(1)
    F = compile (D)
    d = F(A=np.ones(10),B=np.ones(10)*2)

one()  
