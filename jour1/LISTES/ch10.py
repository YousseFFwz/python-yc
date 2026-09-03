donnees = ["Omar", 25, "Casablanca", 15.5, True]

for d in donnees :
    print(type(d))


booll = 0
chaine = 0
nmbr = 0

for d in donnees :
    if type(d) == str :
        chaine += 1
    elif type(d) == bool :
        booll += 1
    elif type(d) == int or type(d) == float :
        nmbr +=1

print(f"ona {chaine} de chaine , {booll} de boolean and {nmbr} de numbers")




numbers = []
for d in donnees : 
    if type(d) == int or type(d) == float :
        numbers.append(d)

print(f"filtrage de list => les nombers : {numbers}")