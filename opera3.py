
import torch

x = torch.tensor (1.0) # la valeur d'entrée
y = torch.tensor (2.0) # la veleur qu'on va prédire

w = torch.tensor (1.0, requires_grad=True)

y_predicted = w * x

loss = (y_predicted -y)**2
print(loss)

loss.backward()
print(w.grad)