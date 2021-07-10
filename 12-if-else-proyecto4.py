#desarrollar una calculadora con las siguientes caracteristicas:
#- Debe manejar las siguientes operaciones matematicas:
#  Suma, resta, multiplicacion, division entera, exponente y modulo.
#  Debe tener un menu de opciones donde el usuario pueda elegir la operacion que desea ejecutar.
#  la calculadora debera solicitar 2 valores por cada operacion.
print("+++++++++++")
print("Calculadora")
print("+++++++++++")
print("Menu de opciones: \n")
print("1. Suma")
print("2. resta")
print("3. Multiplicacion")
print("4. Division")
print("5. Modulo")
print("6. Potencia \n")
opcion = int(input("Elija la opcion 1-6: "))
if opcion == 1:
    print("ud ha elegido suma. \n")
    numero1 = int(input("Ingrese el numero1: "))
    numero2 = int(input("Ingrese el numero2: "))
    resultado = numero1 + numero2
    print("El resultado de la suma es: ", resultado)
elif opcion ==2:
    print("ud ha elegido resta. \n")
    numero1 = int(input("Ingrese el numero1: "))
    numero2 = int(input("Ingrese el numero2: "))
    resultado = numero1 - numero2
    print("El resultado de la resta es: ", resultado)
elif opcion ==3:
    print("ud ha elegido multiplicacion. \n")
    numero1 = int(input("Ingrese el numero1: "))
    numero2 = int(input("Ingrese el numero2: "))
    resultado = numero1 * numero2
    print("El resultado de la multiplicacion es: ", resultado)
elif opcion ==4:
    print("ud ha elegido Division. \n")
    numero1 = int(input("Ingrese el numero1: "))
    numero2 = int(input("Ingrese el numero2: "))
    resultado = numero1 / numero2
    print("El resultado de la division entera es: ", resultado)
elif opcion ==5:
    print("ud ha elegido la operacion 'modulo'. \n")
    numero1 = int(input("Ingrese el numero1: "))
    numero2 = int(input("Ingrese el numero2: "))
    resultado = numero1 - numero2
    print("El resultado de la operacion modulo es: ", resultado)
elif opcion ==6:
    print("ud ha elegido la operacion de potencia. \n")
    numero1 = int(input("Ingrese el numero1: "))
    numero2 = int(input("Ingrese el numero2: "))
    resultado = numero1 ** numero2
    print("El resultado de la operacion potencia es: ", resultado)
else:
    print("Opcion no valida. Vuelva a intentar")
