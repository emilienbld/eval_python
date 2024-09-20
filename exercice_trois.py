class Exo:
    def puissance(self, x, n):
        # Cas de base : toute puissance de 0 est égale à 1
        if n == 0:
            return 1
        # Cas des puissances négatives
        elif n < 0:
            return 1 / self.puissance(x, -n)
        # Cas des puissances positives
        else:
            return x * self.puissance(x, n - 1)

# Tests
exo = Exo()
# Exemple 1
print(exo.puissance(2, 3))
# Résultat attendu : 8

# Exemple 2
print(exo.puissance(2, 1))
# Résultat attendu : 2

# Exemple 3
print(exo.puissance(2, 0))
# Résultat attendu : 1

# Exemple 4
print(exo.puissance(2, -3))
# Résultat attendu : 0.125