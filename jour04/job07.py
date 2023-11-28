#Programme qui compte le nombre de multiples de 3 présents
# dans la liste  L = [8, 24,48,2,16].
L = [8,24,48,2,16]

multipleDe3=0

for x in range(0,5):
    if L[x]%3 == 0:
        multipleDe3+=1

#Affichage du nombre de multiples de 3
print("Le nombre de multiples de 3 de la liste L est de : ",multipleDe3)
