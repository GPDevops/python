#desarrollar un programa que solicite un numero entero desde teclado al usuario,
#posteriormente, el programa debera determinar e indicar a traves de un mensaje,
#si el numero introducido es par o impar.
#Requerimientos:
# - El mensaje debe mostrar la frase el numero es par o impar, 
#   junto con el numero que el usuario introdujo desde teclado
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("determinar si un numero ingresado por teclado es para o impar")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
numero = int(input("Ingrese cualquier numero par: "))
if numero%2 == 0:
    print("El numero ", numero, "es par")
else:
    print("El numero ", numero, "no es par")
print("Fin.")

