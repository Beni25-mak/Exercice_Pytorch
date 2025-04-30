
import torch

weigths = torch.ones(4, requires_grad=True)

for epoch in range(3):
  model_output = (weigths*3).sum()
  model_output.backward()
  
  print(weigths.grad)

  weigths.grad.zero_()

print(weigths)
#print(weigths.grad)
print(model_output)