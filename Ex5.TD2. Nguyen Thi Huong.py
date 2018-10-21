from math import pi
n = int(input("chossi votre nombre "))
produit = 1
for i in range(1, n+1):
    produit = produit * (4 * i ** 2) / ( 4 * i ** 2 - 1)
print ("Cette valeur approchees:", abs(pi / 2 - produit))