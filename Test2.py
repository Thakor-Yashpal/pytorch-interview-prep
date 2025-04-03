import unittest
import torch
import numpy as np



device = 'cuda' if torch.cuda.is_available() else 'cpu'

print(device)

# Import the modules/functions you want to test (adjust the import paths)
# For example:
# from your_project import my_function
# from your_project.models import MyModel


class TestTensorOperations(unittest.TestCase):
    """Tests for basic tensor operations."""

    def test_tensor_creation(self):
        """Test that tensors are created correctly."""
        tensor1 = torch.tensor([1, 2, 3])
        self.assertTrue(torch.equal(tensor1, torch.tensor([1, 2, 3])))  # Checks for equality

        tensor2 = torch.zeros((2, 3))
        self.assertEqual(tensor2.shape, (2, 3))
        self.assertTrue(torch.all(tensor2 == 0))

    def test_tensor_addition(self):
        """Test that tensor addition works correctly."""
        tensor1 = torch.tensor([1, 2, 3])
        tensor2 = torch.tensor([4, 5, 6])
        result = tensor1 + tensor2
        self.assertTrue(torch.equal(result, torch.tensor([5, 7, 9])))

    def test_tensor_multiplication(self):
        """Test that tensor multiplication works correctly."""
        tensor1 = torch.tensor([1, 2, 3])
        result = tensor1 * 2
        self.assertTrue(torch.equal(result, torch.tensor([2, 4, 6])))

    def test_tensor_reshape(self):
        """Test tensor reshaping."""
        tensor = torch.arange(12)
        reshaped_tensor = tensor.reshape(3, 4)
        self.assertEqual(reshaped_tensor.shape, (3, 4))

    def test_tensor_numpy_conversion(self):
        """Test conversion between PyTorch tensor and NumPy array."""
        tensor = torch.tensor([1, 2, 3])
        numpy_array = tensor.numpy()
        self.assertTrue(np.array_equal(numpy_array, np.array([1, 2, 3])))

        # Test conversion back from NumPy to PyTorch
        torch_tensor = torch.from_numpy(numpy_array)
        self.assertTrue(torch.equal(torch_tensor, torch.tensor([1, 2, 3])))

class TestModel(unittest.TestCase):  #Rename appropriately
    """Tests for basic model functionality."""

    def setUp(self):
        """Set up for the tests (e.g., create an instance of your model)."""
        # Example:
        # self.model = MyModel(input_size=10, hidden_size=20, output_size=2)
        # Replace MyModel and the parameters with your actual model class
        pass #Remove this pass when you implement the setup

    def test_model_output_shape(self):
        """Test the output shape of the model."""
        # Example:
        # input_data = torch.randn(1, 10)  # Batch size 1, input size 10
        # output = self.model(input_data)
        # self.assertEqual(output.shape, (1, 2))  # Batch size 1, output size 2
        pass #Remove this pass when you implement the test

    def test_model_forward_pass(self):
        """Test that the forward pass of the model runs without errors."""
        #Ex
        # input_data = torch.randn(1, 10)
        # try:
        #     output = self.model(input_data)
        # except Exception as e:
        #     self.fail(f"Forward pass raised an exception: {e}")
        pass #Remove this pass when you implement the test

    #Add more tests specific to your model's behavior and expected output

if __name__ == '__main__':
    unittest.main()
