ventes = [
    {"produit": "PC", "categorie": "Informatique", "prix": 8000, "quantite": 2},
    {"produit": "Souris", "categorie": "Accessoire", "prix": 150, "quantite": 10},
    {"produit": "Clavier", "categorie": "Accessoire", "prix": 300, "quantite": 5},
    {"produit": "PC", "categorie": "Informatique", "prix": 8000, "quantite": 1},
    {"produit": "Écran", "categorie": "Informatique", "prix": 2500, "quantite": 3}
]

print(f"nomber de vente : {len(ventes)}")

CA = []
for v in ventes :
    CA.append(v["prix"] * v["quantite"] )
print(f"list de CA : {CA}")


max_vente = 0 
produit = None
for v in ventes :
    if v["prix"] > max_vente :
        max_vente = v["prix"] 
        produit = v["produit"]

print(f"le produit cher :{produit} => {max_vente}")


totale_quant_ventes = 0
for v in ventes :
    totale_quant_ventes += v["quantite"]
print(f"totale quntite de ventes : {totale_quant_ventes} ")

list1 = {}
for v in ventes :
    if v["produit"] in list1 :
       list1[v["produit"]] += v["prix"] * v["quantite"]
    else :
       list1[v["produit"]] = v["prix"] * v["quantite"]

print(list1)


list2 = {}
for v in ventes : 
    if v["categorie"] in list2 :
        list2[v["categorie"]] += 1
    else :
        list2[v["categorie"]] = 1

print(list2)