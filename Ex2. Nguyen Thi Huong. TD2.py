a = int(input("Entre votre numbres de copies:"))
Total = 0
if (a <= 10):
    total = 10 * a
elif (a <= 30):
    total = 10 * 10 + (a - 10) * 9
else:
    total = 10 * 10 + 20 * 9 + (a - 30) * 8
print ("total =", total)
