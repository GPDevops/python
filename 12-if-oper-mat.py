#Programa para utilizar los operadores matematicos
#Comparacion de numeros ingresados por teclado con operadores matematicos
print("+++++++++++++++++++++++++++++++++++++++++")
print("Comparar 2 numeros ingresados por teclado")
print("+++++++++++++++++++++++++++++++++++++++++")
numero1 = int(input("Ingrese el 1er. numero: "))
numero2 = int(input("Ingrese el 2do. numero: "))
if numero1 > numero2:
    print("El 1er. numero: ", numero1, " es mayor al 2do. numero: ", numero2)
    print("El 1er. numero: ", numero1, " es diferente al 2do. numero: ", numero2)
elif numero1 < numero2:
    print("El 1er. numero: " + str(numero1) + " es menor al 2do. numero: " + str(numero2))
    print("El 1er. numero: " + str(numero1) + " es diferente al 2do. numero: " + str(numero2))
elif numero1 == numero2:
    print("El 1er. numero: " + str(numero1) + " es igual al 2do. numero: " + str(numero2))
else:
    print("Opcion no valida")
print("Fin.")