
L = [7, 23, 5, 23, 7, 19, 23, 12, 29]

def compterOccurrences(elm, L) :
    for index , l in enumerate(L) :
        if l == elm :
            print(index)


compterOccurrences(5, L)
