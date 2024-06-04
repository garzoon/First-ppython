year = int(input("Ingrese el anho: "))

if year < 1582:
    description = "No dentro del período del calendario Gregoriano"
else:
    if year % 4 != 0:
        description = "es anho comun"
    elif year % 100 != 0:
        description = "es anho bisiesto"
    elif year % 400 != 0:
        description = "es anho comun"
    else:
        description = "es anho bisiesto"

print("El anho", year, description)

print(1 == 1.)
