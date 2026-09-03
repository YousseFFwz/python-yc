notes_etudiants = {"Omar": 15, "Sara": 8, "Yassine": 17, "Imane": 11, "Hamza": 6, "Nadia": 14}

notes_in_10 = {}
notes_sp_10 = {}
for key , val in notes_etudiants.items() :
    if val >= 10 :
        notes_sp_10[key] = val 
    else :
        notes_in_10[key] = val

print(f"etidiant SP 10 : {notes_sp_10}\netidiant IN 10 : {notes_in_10} ")

porsentages = (len(notes_sp_10) / len(notes_etudiants)) * 100 
print(f"le porsentage est : {porsentages} %")
