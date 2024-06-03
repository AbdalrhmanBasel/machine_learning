import torch
import torch.nn as nn
import torch.optim as optim

class LinearRegressionModel(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(LinearRegressionModel, self).__init__()
        self.linear = nn.Linear(input_dim, output_dim)

    def forward(self, x):
        return self.linear(x)


input_dim = 1
output_dim = 1
model = LinearRegressionModel(input_dim, output_dim)

criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)
