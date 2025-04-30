import torch

# initiatisation de la matrice

# mat_1 = torch.zeros(2,3)
# #mat_2 = torch.zeros(12,1)
# #mat_3 = torch.zeros(1,12)

# print(f"Affiche moi la matrice mat_1 : {mat_1}")
#print(f"Affiche moi la matrice créer mat_2: {mat_2}")
#print(f"Affiche moi la matrice créer mat_3: {mat_3}")

# Création d'une matrice unité

# mat_1a = torch.ones(2,3)
# print()
# print(f"Affiche moi la matrice mat_1a : {mat_1a}")

# création d'une matrice qui prend des valeurs aléatoires

# mat_1b = torch.rand(2,3)
# print(f"Affiche moi la matrice mat_1b : {mat_1b}")

# fixe moi cette matrice en prenant le seed = 12

# torch.manual_seed(12)
# mat_1c = torch.randn(2,3)
# print(f"Affiche moi la matrice mat_1b : {mat_1c}")

# Reshape, Transpose and concatenate tensors
# cette fonction va afficher les valeurs aléatoirement maintennant nous allons maintenant quelques choses pour nous permettre d'avoir le même valeurs
# m1 = torch.randint(1,10,(3,3))
# print(f"Affiche la matrice m1 : {m1}")
# # print()
# # print(f"la taille de cette tenseur : {m1.shape}")

# torch.manual_seed(14)
m1a = torch.randint(1,10,(3,3))
# print(f"Afficher les valeurs de la matrice m1a : {m1a}")

# reshape

m2 = m1a.reshape(1,9)
print(m2)

m2 = m1a.reshape(9,1)
print(m2)

m2 = m1a.reshape(1,-1)
print(m2)