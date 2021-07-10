nombre = input("Ingresar su nombre: ")
print("Hola ",nombre, "Este es el resultado de incremento y/o decremento de una variable. ")
valor1 = int(input("Ingresar un valor entero: "))
valor2 = int(input("Ingresar un valor de incremento: "))
valor3 = int(input("ingresar un valor de decremento: "))
print("El valor inicial es: " , valor1)
valor1 +=valor2
print("El valor final de incremento es: " , valor1)
valor1 -=valor3
print("El valor final de decremento es: " , valor1)