import torch

# torch.manual_seed(7)

# mat = torch.randint(1, 10 , (3,3))

# print(mat)

# ## transpose de la matrice

# mat_trans = torch.t(mat)

# # N.B : il y a une différence entre torch.transpose and torch.t

# print(mat_trans)

# concatener deux matrice
torch.manual_seed(4)
A = torch.randint(1,20, (2,2))
print(A)
B = torch.randint(1,5, (2,2))
print(B)
AB = torch.cat((A,B), dim=0)
print(AB)
print(AB.shape)