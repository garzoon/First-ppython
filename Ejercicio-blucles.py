# num = int(input("Inserte un numero: "))
# count = 0
# if num < 0:
#     print("El numero no debe ser menor que 0")
# else:
#     while num != 1:
#         if num % 2 == 0:
#             num = num // 2
#             print(num)
#             count += 1
#         else: 
#             num = 3 * num + 1
#             print(num)
#             count += 1
# print("pasos = ", count)

# blocks = int(input("Ingresa el número de bloques: "))
# height = 0
# blocks_neces = 1 

# while blocks_neces <= blocks:
#     blocks -= blocks_neces
#     height += 1
#     blocks_neces += 1 

# print("La altura de la pirámide:", height)

# for i in range (0, 11):
#     if i % 2 == 0:
#         continue
#     else:
#         print(i)

# x = 1

# while x < 11:
#     if x % 2 == 1:
#         print(x)

#     x += 1

# for ch in "john.smith@pythoninstitute.org":
#     if ch == "@":
#         break
#     else:
#         print(ch)

for digit in "0165031806510":
    if digit == "0":
        print("x")
        continue
    print(digit)
 