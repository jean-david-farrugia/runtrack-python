nom = "Poire"
prix_unitaire = 0.70 
quantité_en_stock = 20

#POUR AJOUTER UNE VARIABLE DANS UNE PHRASE ON UTILISE LA VIRGULE :
print ("Nom = ", nom)
print ("Prix à l'unité = ", prix_unitaire)
print ("Quantité en stock = ", quantité_en_stock)

print(f"Le produit {nom} qui a un prix unitaire de {prix_unitaire} " ,
       " et dont la quantité en stock est de : {quantité_en_stock}")

# On demande à l'utilisateur de saisir une quantité
reponse_user = input(f"Combien de {nom} voulez-vous acheter ?")

# On affiche sa réponse 
print(reponse_user)
quantité_restante = (quantité_en_stock - int(reponse_user))

# On soustrait la réponse à la quantité de départ
print (f"La quantité restante est égale à : {quantité_restante}")

#On ajoute des produits au stock de départ
print(f"Ajoutez des {nom} en stock :")
quantité_ajoutée = input(f"Combien de {nom} voulez-vous rajouter ?")

nouvelle_quantité = quantité_en_stock + int(quantité_ajoutée)

print(f"La quantité totale est de : {nouvelle_quantité}")

# Inflation du produit : 
nouveau_prix_unitaire = (prix_unitaire + prix_unitaire * 0.1)
print(f"Nouveau prix après inflation de 10% : {nouveau_prix_unitaire}")

# Après mise à jour du nouveau stock : 
print("Stock mis à jour : ")
print ("Nom = ", nom)
print ("Prix à l'unité après inflation = ", nouveau_prix_unitaire)
print ("Quantité en stock = ", nouvelle_quantité)

