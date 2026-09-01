number = int(input("entrer un number :"))



while True :
    if number == 1 :
        break 

    elif number % 2 == 0 :
        number = number // 2
    
    elif number % 2 != 0 :
        number = number * 3 + 1
    
print(number)

