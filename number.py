import torch

X = torch.tensor(5)
Y = torch.tensor(10)
Z = torch.tensor(70)

print(f"Afficher la valeur de X : {X}")
print(f"Afficher la valeur de Y : {Y}")
print(f"Afficher la valeur de Z : {Z}")

### opérations avec les numbers

print(f"Affiche moi l'addition entre X et Y : {X+Y}")
print(f"Affiche moi la multiplication entre X et Y : {X*Y}")
print(f"Affiche moi la soustraction entre X et Y:{X-Y}")
print(f"Affiche moi la division entre Z et X: {Z/X}")
print(f"Affiche moi la division entre Y et X: {Y/X}")

#torch.help