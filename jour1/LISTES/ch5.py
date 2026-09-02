scores = [45, 12, 78, 34, 90, 23, 67, 56, 89, 10]

 

# Afficher la liste originale, puis créer une copie 
# list1 = [] 
# for s in scores :
#     list1.append(s)
# print(f"{list1}  / {scores}")

list1 = scores.copy()
print(f" {list1}")




# Trier la première copie dans l'ordre croissant et une deuxième copie dans l'ordre décroissant
scores.sort()
print(scores)

list1.sort(reverse=True)
print(list1)





# Afficher les deux résultats ainsi que les trois meilleurs scores
print(scores)
print(list1)

for index , elm in enumerate(list1) :
    if index < 3 :
        print(elm)

    