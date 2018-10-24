ch = input("entre une chaine de caractere:")
un = input("entre un caractere")
deux = input("entre un second caractere: ")
res = ""
for c in ch:
    if (c == un):
        res += deux
    elif (c == deux):
        res += un
    else:
        res += c
print(res)

