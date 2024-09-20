# Fonction qui trouve tous les groupes de 3 éléments dans une liste dont la somme est égale à 0.
def trouver_groupes_zero(liste):
    resultats = []  # Liste pour stocker les groupes dont la somme est égale à 0
    liste.sort()  # Tri de la liste pour faciliter la recherche avec deux pointeurs

    # Parcours de chaque élément de la liste jusqu'à l'avant-dernier élément
    for i in range(len(liste) - 2):
        # Si l'élément actuel est le même que le précédent, on saute cette itération pour éviter les doublons
        if i > 0 and liste[i] == liste[i - 1]:
            continue
        
        gauche = i + 1  # Initialisation du pointeur gauche juste après l'élément courant
        droite = len(liste) - 1  # Initialisation du pointeur droit à la fin de la liste

        # Boucle tant que les pointeurs gauche et droite ne se croisent pas
        while gauche < droite:
            somme = liste[i] + liste[gauche] + liste[droite]  # Somme des trois éléments courants
            
            if somme == 0:
                # Si la somme est égale à 0, on ajoute ce groupe aux résultats
                resultats.append([liste[i], liste[gauche], liste[droite]])

                # Avancer le pointeur gauche tout en évitant les doublons
                while gauche < droite and liste[gauche] == liste[gauche + 1]:
                    gauche += 1
                # Reculer le pointeur droit tout en évitant les doublons
                while gauche < droite and liste[droite] == liste[droite - 1]:
                    droite -= 1
                
                # Avancer les deux pointeurs pour explorer d'autres combinaisons
                gauche += 1
                droite -= 1
            
            elif somme < 0:
                # Si la somme est inférieure à 0, on avance le pointeur gauche pour augmenter la somme
                gauche += 1
            else:
                # Si la somme est supérieure à 0, on recule le pointeur droit pour diminuer la somme
                droite -= 1

    return resultats  # Retourne la liste des groupes trouvés

# Fonction qui affiche les résultats des groupes de 3 éléments dont la somme est égale à 0.
def afficher_resultats(liste):
    resultats = trouver_groupes_zero(liste)
    
    if resultats:
        print(f"Groupes de somme égale à 0 : {resultats}")
    else:
        print("Aucun groupe de 3 éléments n'a une somme égale à 0.")

# Exemple 1
liste1 = [2, 7, 9, -9]
print(f"Liste entrée : {liste1}")
afficher_resultats(liste1)
# Résultat attendu :
# Liste entree : [2, 7, 9, -9]
# Groupes de somme egale a 0 : [[-9, 2, 7]]

# Exemple 2
liste2 = [-33, -10, -8, -2, 1, 4, 9, 10]
print(f"Liste entrée : {liste2}")
afficher_resultats(liste2)
# Résultat attendu :
# Liste entree : [-33, -10, -8, -2, 1, 4, 9, 10]
# Groupes de somme egale a 0 : [[-10, 1, 9], [-8, -2, 10]]

# Exemple 3 (sans résultats)
liste3 = [1, 2, 3, 4, 5]
print(f"Liste entrée : {liste3}")
afficher_resultats(liste3)
# Résultat attendu :
# Liste entree : [1, 2, 3, 4, 5]
# Aucun groupe de 3 elements n'a une somme egale a 0.
