Notes = [12, 4, 14, 11, 18, 13, 7, 10, 5, 9, 15, 8, 14, 16]

# Afficher toutes les notes.
print(f"toutes les notes : {Notes}")



# Calculer la moyenne
somme = 0 
for x in Notes :
    somme += x
moyenne = somme / len(Notes)
print(f"la moyenne est : {moyenne}")





# Créer une liste contenant les notes supérieures à la moyenne.
list1 = []
for n in Notes :
    if n > moyenne :
        list1.append(n)
print(list1)




# Créer une liste contenant les notes inférieures à la moyenne.
list2 = []
for n in Notes :
   if n < moyenne :
       list2.append(n)
print(list2)





# Trouver la meilleure note et la plus mauvaise note.

meilleure = 0
for n in Notes :
    if n > meilleure :
        meilleure = n
print(f"la meilleure note  est : {meilleure}")

mauvaise = float('inf')
for n in Notes :
    if mauvaise > n :
        mauvaise = n
print(f"la mauvaise note  est : {mauvaise}")







# Compter le nombre de notes supérieures ou égales à 10 et calculer le pourcentage de réussite.
cmp = 0 
for n in Notes :
    if n > moyenne :
        cmp += 1

pourcentage = (cmp / len(Notes)) * 100
print(f" le pourcentage est : {pourcentage} %")