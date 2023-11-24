#Programme qui affiche tous les nombres de 0 à 100 
#sauf 26, 37 et 88
nombre = 0
for nombre in range (0, 101):
    
    if nombre == 26 or nombre == 37 or nombre == 88:
        #print("Ce nombre ne doit pas s'afficher !")
        continue
    else:        
        print("Le nombre vaut : ", nombre)

