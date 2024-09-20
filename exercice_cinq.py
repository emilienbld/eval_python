def plus_petit_plus_grand():
    print("Mémorisez un nombre entier entre 1 et 100, le script va essayer de le retrouver.")
    
    # Initialisation des bornes inférieure (bas) et supérieure (haut)
    bas = 1
    haut = 100
    nb_coups = 0  # Compteur pour suivre le nombre d'essais
    incoherence = False  # Indicateur pour détecter la tricherie

    while bas <= haut:  # Tant que l'intervalle est valide
        proposition = (bas + haut) // 2  # Le script propose le milieu de l'intervalle actuel
        nb_coups += 1  # On incrémente le compteur à chaque essai
        
        print(f"Script propose {proposition}... +, - ou G ? ", end="")
        reponse = input().strip()  # L'utilisateur doit indiquer si c'est plus grand, plus petit, ou trouvé

        if reponse == "G":  # Si l'utilisateur indique que le script a trouvé le bon nombre
            print(f"Script a trouvé {proposition} en {nb_coups} coups !!!")
            break  # Sortir de la boucle, car le script a trouvé le nombre
        elif reponse == "+":  # Si l'utilisateur indique que le nombre est plus grand
            bas = proposition + 1  # Ajuste la borne inférieure
        elif reponse == "-":  # Si l'utilisateur indique que le nombre est plus petit
            haut = proposition - 1  # Ajuste la borne supérieure
        else:
            print("Réponse invalide. Merci de répondre par +, - ou G.")  # En cas de réponse incorrecte
            continue  # Revenir au début de la boucle pour reproposer

        # Si la borne inférieure dépasse la borne supérieure, il y a incohérence
        if bas > haut:
            incoherence = True
            break
    
    if incoherence:
        print("Tricheur !!! Vous avez répondu de manière incohérente.")
    elif nb_coups > 0:
        print(f"Script a trouvé votre nombre en {nb_coups} coups !")

# Appel de la fonction pour démarrer le jeu
plus_petit_plus_grand()
