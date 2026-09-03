niveux = [5, 4, 3, 4] 
noms = ["Python", "SQL", "Pandas", "NumPy"] 

list1 = {}
for n in range(len(noms)) :
    list1[noms[n]] = niveux[n] 

print(list1)