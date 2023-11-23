def pair_ou_impair(nombre):
    #On vérifie si le nombre est entier et positif
    if nombre > 0 and nombre %2 == 0:
        print("Le nombre est pair ")
    elif nombre %2 !=0:
        print("Le nombre est impair")

# On appelle la fonction plusieurs fois
# avec des valeurs différentes.

pair_ou_impair(10)
pair_ou_impair(5)