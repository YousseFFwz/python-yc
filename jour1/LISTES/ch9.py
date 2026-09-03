text1 = "Python est un langage de programmation tres puissant et simple"
text2 = "Le langage Python est utilise pour la programmation web et le code"
list1 = []
for word in text1.split() :
    wordLower = word.lower() 
    if len(wordLower) > 3 :
     list1.append(wordLower)


list2 = []
for word in text2.split() :
   wordLower = word.lower() 
   if len(wordLower) > 3 :
      list2.append(wordLower)


word_comuns = []
for wrd in list1 :
   if wrd in list2 and wrd not in word_comuns :
      word_comuns.append(wrd) 

print(f"les words commun est : {word_comuns}")