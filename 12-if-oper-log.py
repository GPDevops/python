#uso de operadores logicos and/or/not
print("++++++++++++++++++++++++++++++++++++")
print("Uso de operadores logicos and/or/not")
print("++++++++++++++++++++++++++++++++++++")
print("Uso de operador logico 'OR': ")
numero1 = int(input("Ingrese el 1er. numero de 0 a 9: "))
numero2 = int(input("Ingrese el 2do. numero de 0 a 9: "))
print("Los numeros a comparar son: ", numero1, " y ", numero2)
if numero1 > numero2 or numero2 < 7:
    print("la condicion 'OR' se ha cumplido \n")
else:
    print("la condicion 'OR' no se cumple \n")
print("Uso de operador logico 'AND': ")
palabra = input("ingresar un numero en letras: ")
numero3 = int(input("Ingresar el numero anterior en numeros: "))
print("Los numeros y letras a comparar son: ", palabra, " y ", numero3)
if palabra == 'uno' and numero3 == '1':
    print("la condicion 'AND' se ha cumplido \n")
else:
    print("la condicion 'AND' se ha cumplido \n")
print("Uso de operador logico 'NOT': ")
numero4 = int(input("Ingrese un numero del 1-5: "))
print("El numero a comparar es: ", numero4)
if not numero4 == 5:
    print("El numero cumple la condicion 'NOT'")
else:
    print("El numero NO cumple la condicion 'NOT'")
print("Fin. \n")