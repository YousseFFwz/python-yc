Langages = ["Python", "Java", "JavaScript", "C++"]
# Ajouter "PHP" à la fin
Langages.append("php")
print(Langages)


# Ajouter "SQL" à la fin
Langages.append("sql")
print(Langages)

# Insérer "C" en deuxième position
Langages.insert(1,"c")
print(Langages)




# Supprimer "Java" .
Langages.remove("Java")
print(Langages)

# Supprimer le dernier élément.
Langages.pop()
print(Langages)

# Afficher la liste finale et le nombre d'éléments.
print(f"la list finale est {Langages} et le nomber delemetents est {len(Langages)}")