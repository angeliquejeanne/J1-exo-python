import random

print("Bienvenue dans le jeu !")

# Choix du niveau de difficulté
level = int(input(" Ecrit 1:facile, 2:moyen, 3:difficile"))


# Compteur de clés magique
keys = 0

# Répéter les manches de notre jeu
while keys != 3 :

    print("Vous disposez de 5 jarres devant vous. Choisissez 1, 2, 3, 4 ou 5")

    # tableau qui va contenir chacune des jarres
    jars = ['K', 'K', 'K', 'K', 'K']

    # Boucle qui va tournée autant de fois qu'il doit y avoir de serpents
    for i in range(0, level):
        print("1 serpent & été ajouter dans une jarre")
        jars[i] = 'S'
    # Melange les jarres
    random.shuffle(jars)

    # Demande à notre joueur de mettre une valeur
    choice = int(input())

    print ("Le joueur a mit la jarre n°", choice)

    # Vérification
    if jars[choice-1] == 'K': #gagné
        print("Gagné ! Tu obtiens une clé magique ! La jarre infécté était la", jars)
        keys += 1
        print("Vous avez actuellement", keys, "/3 clés")
    else:
        print("Perdu ! un serpent apparaît !")
        
        # Si le joueru n'a pas de clé
        if keys > 0:
            keys -= 1
            print("Vous avez actuellement", keys, "/3 clés")

print("Tu deviens le roi du temple !")