# Fonction convertit une liste de chiffres en un entier.
def liste_to_entier(liste):
    nombre = 0  # Initialise un entier à 0
    for chiffre in liste:
        # Pour chaque chiffre de la liste, on déplace les chiffres précédents d'un rang
        # et on ajoute le nouveau chiffre à la fin
        nombre = nombre * 10 + chiffre
    return nombre  # Retourne le nombre entier obtenu

# Fonction convertit un entier en une liste de chiffres.
def entier_to_liste(nombre):
    if nombre == 0:
        return [0]  # Si le nombre est 0, on retourne [0] directement
    
    resultat = []  # Initialise une liste pour stocker les chiffres du nombre
    while nombre > 0:
        # Extrait le dernier chiffre (modulo 10) et on l'ajoute à la liste
        resultat.append(nombre % 10)
        # Retire le dernier chiffre du nombre (division entière par 10)
        nombre //= 10
    
    resultat.reverse()  # On inverse la liste car les chiffres sont ajoutés dans l'ordre inverse
    return resultat  # Retourne la liste des chiffres

# Fonction prend deux listes de chiffres (n1 et n2), les convertit en entiers, les additionne, 
# puis retourne le résultat sous forme de liste de chiffres.

def addition_listes(n1, n2):
    # Convertit les deux listes de chiffres en nombres entiers
    nombre1 = liste_to_entier(n1)
    nombre2 = liste_to_entier(n2)
    
    # Additionne les deux entiers obtenus
    total = nombre1 + nombre2
    
    # Convertit le total en liste de chiffres
    return entier_to_liste(total)

# Exemple 1
print(addition_listes([8, 4, 0], [8, 3]))
# Résultat attendu : [9, 2, 3]
# Explication : 840 + 83 = 923, donc [9, 2, 3]

# Exemple 2
print(addition_listes([1, 8, 3], [7]))
# Résultat attendu : [1, 9, 0]
# Explication : 183 + 7 = 190, donc [1, 9, 0]

# Exemple 3
print(addition_listes([1, 2, 3], [0]))
# Résultat attendu : [1, 2, 3]
# Explication : 123 + 0 = 123, donc [1, 2, 3]
