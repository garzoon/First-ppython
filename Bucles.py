# Contador de numeros impares

par = 0
impar = 0

num = int(input("escriba un numero o 0 para finalizar"))

while num != 0:
    if num & 2 == 0:
        par += 1
    else:
        impar += 1
print("pares:", par)
print("Impares:", impar)
