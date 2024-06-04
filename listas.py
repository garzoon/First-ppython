# # crear lista en python
numbers = [19.8, 1, 123, 4, 5, 10, 43]

# print(numbers[0])

# numbers[3] = 101
# numbers[4] = numbers[1]

# print(len(numbers))

# # eliminar un elemento de una lista
# del numbers[0]
# print(numbers)
# print(len(numbers))

# # valores negativos de una lista
# # <-----------------|
# # [1, 4, 5, 10, 19.8]
# print(numbers[-1])

# # Insertar valores en una lista

# #append == este agrega un valor al final de la lista
# numbers.append(56)
# print(numbers)


# # Insert == En inster escogemos la posocion donde sera agergado el dato
# numbers.insert(0, 45)
# print(numbers)

# # creacion de listas vacias 

# list = []

# for i in range (5):
#     list.append(i + 1)
# print(list)


# # las lista y los ciclos for
 
# mylist = [2, 4, 2, 54, 12]
# total = 0 

# for i in range(len(mylist)):
#     total += mylist[i]
# print(total)

# invertir valores en python

# queremos invertir los valores que el v0 ahora sea el v3

# otherList = [23, 12, 453, 5]
# print(otherList)
# otherList[0], otherList[3] = otherList[3], otherList[0]
# print(otherList)


# Hacer que python ordene listas 

# print(numbers)
# numbers.sort()
# print(numbers)

# # Revertir una lsita

# numbers.reverse()
# print(numbers)

# rebanasdas de listas

# una lista crea un espacio en la memoria y cuando hacemos una copia esta tambien va acupar dicho espacio 

#                start:end-1
# new_numbers = numbers[0:3]
# print(new_numbers)

# # copiar toda la lista

# new_numbers = numbers[:]
# print(new_numbers)

# # eliminar rebanadas

# del new_numbers[2:4]
# print(new_numbers)

# Operadores in y not in

# elemento in lista : Buscar un elemento en dicha lista, si existe, devuelve True 

# elemento not in lista : Buscar un elemento en dicha lista, si NO existe, devuelve True

# my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
# new_list = []

# for i in my_list:
#     if i not in new_list:
#         new_list.append(i)

# print("La lista con elementos únicos:")
# print(new_list)


# squares = [x ** 2 for x in range(10)]
# print(squares)
my_list = [i for i in range(-1, 2)]

print(my_list)






