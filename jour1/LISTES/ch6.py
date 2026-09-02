L = [10, 20, 30, 40, 50]

def rechercheElement(elment , list ) :
    for l in list :
        if l == elment :
            print(l)
            break
    else :
         print("false") 


rechercheElement(100 , L )