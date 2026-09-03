produit = {
    "nom": "Ordinateur", "prix": 8500,
    "stock": 12, "categorie": 
"Informatique"
}

produit["prix"] = 9700
produit["marque"] = "lenovo"
produit["disponile"] = "true"
print(produit)
del produit["stock"]
print(produit)
produit.pop("categorie")
print(produit)



