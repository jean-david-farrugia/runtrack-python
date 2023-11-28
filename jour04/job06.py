#Programme qui échange les valeurs de la première et de la dernière case
#d’une liste quelconque non vide.
#Exemple de liste quelconque à 7 valeurs :
maListe=['tonton_debut',1,2,3,4,5,'tonton_fin']

print("La liste de début est : ",maListe)

indice_fin = len(maListe)-1
#Echange entre la première et dernière valeur de la liste 
temp = maListe[0]
maListe[0]=maListe[indice_fin]
maListe[indice_fin]  = temp

print("La liste de fin est : ",maListe)


