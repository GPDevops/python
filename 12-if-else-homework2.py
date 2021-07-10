## Convertidor de numeros a letras - las vocales
print("++++++++++++++++++++++++++++++++++++++++++++++")
print("Convertir los numeros de las vocales en letras")
print("++++++++++++++++++++++++++++++++++++++++++++++")
a = int(input("Ingrese el numero en el rango del 1-5: "))
if a == 1:
    print("El numero es: " + str(a) + " equivale a la letra: 'a'")
elif a == 2:
    print("El numero es: " + str(a) + " equivale a la letra: 'e'")
elif a == 3:
    print("El numero es: " + str(a) + " equivale a la letra: 'i'")
elif a == 4:
    print("El numero es: " + str(a) + " equivale a la letra: 'o'")
elif a == 5:
    print("El numero es: " + str(a) + " equivale a la letra: 'u'")
else:
    print("Error! los numeros van del 1 al 5")
