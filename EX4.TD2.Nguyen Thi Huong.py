a = int(input("choissi votre nombre"))
b = int(input("choissi votre autre nombre plus petit"))
somme = 0
for x in range(a + 1, b):
    k = x ** 3
    somme = somme + k
print(somme)



