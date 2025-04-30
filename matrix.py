import torch

a = torch.tensor (
[
    [1,2],
    [4,3],
    [4,70]
]
)

b = torch.tensor (
    [
        [2,3],
        [12,13],
        [1,0]
    ]
)

#print(f"Afficher la matrice : {a}")
#print(f"afficher la taille de la matrice : {b.shape}")
#print()
#print(f"Afficher la matrice : {b}")
#print(f"Afficher la taille de la matrice : {b.shape}")

#print(f"Affiche la somme de la matrix a et b : {a+b}")
#print(f"Affiche la soustraction entre la matrix b et a: {b-a}")
#print(f"Affiche la division entre la matrice b/a: {b/a}")
#print(f"Afficher la division entre la matrice a/b: {a/b}")

d = torch.div(a,b)  #division de deux matrices
print(f"affiche moi: {d}")
de = torch.div(b,a) # division de deux matrices
print(de)
m = torch.mul(a,b)
print(m)
add = torch.add(a,b)
print(add)
sustraction = torch.sub(a,b)
print(sustraction)
sust = torch.sub(b,a)
print(sust)