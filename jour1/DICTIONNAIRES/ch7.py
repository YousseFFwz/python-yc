etudiants = [
    {"nom": "Omar", "age": 22, "note": 15},
    {"nom": "Sara", "age": 21, "note": 17},
    {"nom": "Yassine", "age": 23, "note": 9},
    {"nom": "Imane", "age": 20, "note": 13},
]

for e in etudiants :
    if e["note"] > 10 :
        print(f"{e["nom"]} : admis")
    else :
        print(f"{e["nom"]} : échec")

somme = 0
for e in etudiants :
   somme += e["note"] 

moyenne = somme / len(etudiants)
print(f"le moyenne : {moyenne}")


N_max = 0
for e in etudiants :
    if e["note"] > N_max :
        N_max = e["note"]

print(f"le millieur note est : {N_max}")