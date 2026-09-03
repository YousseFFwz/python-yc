etudiant = {
    "nom": "Omar", "age": 22,
    "ville": "Casablanca", "note": 15
}

print(f"nom : {etudiant['nom']} \nage : {etudiant['age']} \nville : {etudiant['ville']} \nnote : {etudiant['note']}")

etudiant["note"] = 17
etudiant["formation"] = "AI"
print(f"MODFICATION \nnom : {etudiant['nom']} \nage : {etudiant['age']} \nville : {etudiant['ville']} \nnote : {etudiant['note']} \nformation : {etudiant['formation']}")