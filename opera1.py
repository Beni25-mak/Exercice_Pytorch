import torch

# # # calcul de Autograd

# # # X = torch.randn(3, requires_grad = False)
# # x = torch.tensor(3.0, requires_grad=True)
# # #y = 3 * X
# # y = x + 2

# # # definition de z en fonction de y
# # z = 6 * y

# # # definition de h en fonction de z

# # h = (1/3) * z

# # # print(f"Affiche les valeurs de X : {X}")
# # # print(f"Affiche les valeurs de la fonction y : {y}")
# # # print(f"Affiche les valeurs de la fonction z : {z}")
# # # print(f"Affiche les valeurs de la fonction h : {h}")

# # # Calcul du gradient

# # h.backward()

# # print(x.grad)

# # # affichage du gradient

# # print(f"dh/dx at x=3: {x.grad}")

# # deuxième exemple pour calculer le gradient d'une fonction

# x = torch.tensor(2.0, requires_grad=True) ## notre tensor x est de type number

# y = x ** 2

# print(y)

# # Calcul du gradient dy/dx

# y.backward()

# # Affichage du gradient (dy/dx = 2x = 4)
# print(f"le gradient de dy/dx : {x.grad}")  

# # troisième exemple pour calculer le gradient d'une fonction
# # et tracer les fonctions

# t = torch.tensor(5.0, requires_grad=True)

# # fonction complexe : y = t^2 + 10t -5

# y = t**2 + 10*t -5


# # fonction complexe : z = 15 + y^2
# z = 15 + y**2

# # calcul du gradient dz/dy

# z.backward()

# # affichage du gradient

# print(f"le gradient de dz/dy : {t.grad}")


## 4e exercice

t = torch.tensor(2.0, requires_grad=True)

y = torch.exp(t) + 3*(t**2) - t
z = y**2 + 4

#print(t)
#print(y)
#print(z)

z.backward()

print(f"la fonction dz/dt : {t.grad}")