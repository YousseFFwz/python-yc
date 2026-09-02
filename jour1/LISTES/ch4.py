temperatures = [18, 25, 31, 14, 27, 35, 22, 19, 30, 12, 28]


# Créer une liste des températures > 25.
list1 = []
for t in temperatures :
    if t > 25 :
        list1.append(t)
print(f"liste des températures > 25. :  {list1}")





# Créer une liste des températures ≤ 25.

list2 = [] 
for t in temperatures :
    if t <= 25 :
        list2.append(t)
print(f"liste des températures ≤ 25. :  {list2}")



# Créer une liste des températures comprises entre 20 et 30 inclus 

list3 = []
for t in temperatures :
    if t < 30 and t > 20 :
        list3.append(t)
print(f"liste des températures comprises entre 20 et 30 :  {list3}")






# Compter le nombre de températures supérieures à 30.
cmp = 0
for t in temperatures :
    if t > 30 :
        cmp += 1
print(f"le nombre de températures supérieures à 30. : {cmp}")