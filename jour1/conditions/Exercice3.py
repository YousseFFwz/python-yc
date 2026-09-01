name = input("entrer votre nom :")
age = int(input("entrer votre age :"))
if age < 18 :
    print( "lentrée est refusée")
elif age >= 18 and age < 25 :
    print( " l'entrée est gratuite")
else :
    print(name , " l'entrée est autorisée uniquement si elle est membre du club ouaccompagnée d'un membre")