#Desarrollar un programa que solicite tres numeros enteros desde teclado al usuario,
#posteriormente, el programa debera determinar e indicar a traves de un mensaje
#en pantalla, cual de los tres numeros es el mas grande.
#Requerimientos:
# - El mensaje en pantalla debera mostrar el numero que resulto ser el mas grande los 3.
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("De 3 numeros ingresados por teclado, indicar cual es el mayor")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
numero1 = int(input("Ingresar el 1er. numero: "))
numero2 = int(input("Ingresar el 2do. numero: "))
numero3 = int(input("Ingresar el 3er. numero: "))
if numero1 > numero2 and numero1 > numero3:
    print("El numero, ", numero1, + " es el mas grande de todos")
else:
    if numero2 > numero3:
        print("El numero, ", numero2, " es el mas grande de todos")
    else:
        print("El numero, ", numero3, " es el mas grande todos")
