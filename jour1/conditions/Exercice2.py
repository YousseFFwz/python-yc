# Exercice 2 — Calcul du salaire
nomEmploye = input("nom d'un employé :")
salaireHoraire = int(input("salaire horaire :"))
heuresTravaillees = int(input("le nombred'heures travaillées :"))
salaire = salaireHoraire * heuresTravaillees
if salaire > 40 :
     Heures = salaire - 40 
     salaireRemunerees = Heures * 1.5
     print("salaire totale de " ,nomEmploye , " est :" ,salaire + salaireRemunerees )

