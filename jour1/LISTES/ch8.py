

L = [7, 23, 5, 23, 7, 19, 23, 12, 29, 7, 5]
list1 = {}

for l in L :
    if l in list1 :
        list1[l] += 1
    else :
        list1[l] = 1

print(list1)