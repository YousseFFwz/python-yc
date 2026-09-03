notes = {"Python": 15, "SQL": 13, "JavaScript": 17, "Git": 14, "Linux": 12}

print(notes.keys())
print(notes.values())

for key , val in notes.items() :
    if val % 2 == 0 :
        print(f"{key} : {val}")