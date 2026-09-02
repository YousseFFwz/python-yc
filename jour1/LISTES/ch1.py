fruits = ["Pomme", "Banane", "Orange", "Fraise", "Mangue", "Kiwi"]



# Afficher la liste complète
print(f"la liste complete  : {fruits}")


# Afficher le premier élément
print(f"la premier element est : {fruits[0]}")


# Afficher le dernier élément
print(f"Afficher le dernier élément est : {fruits[len(fruits)-1]}")


# Afficher le troisième élément
print(f"le troisième élément est : {fruits[2]}")




# Afficher les trois premiers éléments.
print("les trois premiers éléments")
for index , elem in enumerate(fruits) :
    if index < 3 :
      print(f"element {index+1}  est : {elem}")
 
# Afficher les trois derniers éléments.
print("les trois derniers éléments")
for index , elem in enumerate(fruits) :
    if index == len(fruits)-1 or index == len(fruits)-2 or index == len(fruits)-3 :
       print(f"elemnt est : {elem} ")

# Afficher un élément sur deux.
print("un élément sur deux")
for index , elm in enumerate(fruits) :
    if index % 2 != 0 :
      print(f"l'élément sur deux nombre {index+1} est : {elm}")




# Remplacer "Orange" par "Ananas" .

print("Remplaceremnt Orange par Ananas")


for index , elm in enumerate(fruits) :
    if elm == "Orange" :
        fruits[index] = "anans"

# Afficher la liste après modification.
print(f" la list apres modification : \n {fruits}")
