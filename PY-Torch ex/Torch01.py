import torch.nn as nn

model =nn.Sequential(
    nn.Linear(8,2),
    nn.ReLU(),
    nn.Linear(12,8),
    nn.ReLU(),
    nn.Linear(8,1),
    nn.Sigmoid()
)

print(model)

# what is this code output on

