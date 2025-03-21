import torch
import torch.nn as nn

class MyModel(nn.Module):
    def __init__(self, input_size, hidden_neurons):  # Pass input_size as an argument
        super(MyModel, self).__init__()

        self.input_layer = nn.Linear(input_size, hidden_neurons) # No X.shape dependency
        self.linear = nn.Linear(hidden_neurons, 1)  # Output a single value
        self.activation = nn.ReLU() # Remove the argument 1
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        # Correct placement of activation function
        x = self.input_layer(x)
        x = self.activation(x)
        x = self.linear(x)
        x = self.sigmoid(x)
        return x

# Example Usage (after the class definition):
if __name__ == '__main__':
    # Dummy data for demonstration
    input_size = 10  # Example input size (number of features)
    hidden_neurons = 50
    X = torch.randn(100, input_size)  # Example input data (100 samples, input_size features)

    # Instantiate the model
    model = MyModel(input_size, hidden_neurons)

    # Pass the input through the model
    output = model(X)

    # Print the output shape
    print("Output shape:", output.shape) # Verify the output size.  Should be torch.Size([100, 1])