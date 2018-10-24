array = [3,4,2,2,6,3,6,6,5,7]
output = []
temp = 0
for i in range(0, len(array)):
    if i % 2 == 0:
        temp = array[i]
    else:
        temp = temp + array[i]
        output.append(temp)
print(output)
#array[i] est l'element d'indice i dans array
#(le i + 1 eme element)
suite = eval(input("entre ume suite pair"))
a = []
l = len(suite) #len renvoie la longueur du tuple
for i in range(0,l,2): #from  0 to l (0,l)et the programme do couple number et couple nomber (2)
    a = (suite[i] + suite[i + 1])
print(a)
#res += 1 means res = res +1
