def Huong(array):
    output = []
    temp = 0
    for i in range(0, len(array)) :
        if i % 2 == 0:
            temp = array[i]
        else:
            temp = temp + array[i]
            output.append(temp)
    return output
nombres = [3,4,2,2,6,3,6,6,5,7]
neauveau_nombres = Huong(nombres)
print(nombres)
print(neauveau_nombres)

