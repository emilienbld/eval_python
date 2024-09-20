# Cette fonction prend une phrase en entrée et renvoie deux listes
def separer_phrase(phrase):
    mots = []         # Liste pour stocker les mots de la phrase
    separateurs = []  # Liste pour stocker les séparateurs (espaces, virgules, ...)
    mot = ''          # Chaîne temporaire pour construire un mot au fur et à mesure
    
    for char in phrase:
        if char.isalnum() or char == "'":  # Si le caractère est une lettre, un chiffre ou une apostrophe
            mot += char                    # Construit le mot en ajoutant le caractère
        else:
            if mot:                        # Si un mot a été construit, ajoute à la liste des mots
                mots.append(mot)
                mot = ''                   # Réinitialise la variable pour le prochain mot
            separateurs.append(char)       # Le caractère est un séparateur (espace, virgule, etc.)
    
    if mot:                                # Si un mot est resté à la fin, on l'ajoute à la liste des mots
        mots.append(mot)

    return [mots, separateurs]  # Retourne deux listes : les mots et les séparateurs

# Exemple 1
phrase_1 = "J'ai découvert Python cette semaine"
print(separer_phrase(phrase_1))
# Résultat attendu :
# [["J'ai", "découvert", "Python", "cette", "semaine"], [" ", " ", " ", " ", " "]]

# Exemple 2
phrase_2 = "J'ai découvert Python, cette semaine"
print(separer_phrase(phrase_2))
# Résultat attendu :
# [["J'ai", "découvert", "Python", "cette", "semaine"], [" ", " ", ", ", " ", " "]]

# Exemple 3
phrase_3 = "J'ai découvert, Python, cette semaine"
print(separer_phrase(phrase_3))
# Résultat attendu :
# [["J'ai", "découvert", "Python", "cette", "semaine"], [" ", ", ", ", ", " ", " "]]
