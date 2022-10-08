# programa para convertir un numero (1-5) a letras y vicerversa
# usando sentencias condicionales anidadas if - elif
print ("+++++++++++++++++++++++++++++++++++++++++++++++")
print ("CONVERSOR DE NUMEROS '1-5' A LETRAS y VICEVERSA")
print ("+++++++++++++++++++++++++++++++++++++++++++++++ \n")
print ("Ingrese la opcion que requiere: \n '1 = conversor de numeros a letras o 2 = conversor de letras a numeros'")
opcion = int(input("Ingrese la opcion: "))
#print(opcion)
if opcion == 1:
    print("Ud a elegido la opcion de conversor de numeros a letras: ")
    opcion1 = int(input("Ingrese el numero del 1-5 a convertir: "))
    if opcion1 == 1:
        print("El numero ingresado es: 'uno'")
    elif opcion1 == 2:
        print("El numero ingresado es: 'dos'")
    elif opcion1 == 3:
        print("El numero ingresado es: 'tres'")
    elif opcion1 == 4:
        print("El numero ingresado es: 'cuatro'")
    elif opcion1 == 5:
        print("El numero ingresado es: 'cinco1'")
    else:
        print("El numero elegido no esta en el rango del 1-5. Vuelva a intentar! \n")    
elif opcion == 2:
    print("Ud a elegido la opcion de conversor de letras a numeros: \n")
    opcion2 = input("Ingrese el numero en letras: ")
    opcion2 = opcion2.lower()
    if opcion2 == 'uno':
        print("El numero en letras ingresado equivale al numero: '1'")
    elif opcion2 == 'dos':
        print("El numero en letras ingresado equivale al numero: '2'")
    elif opcion2 == 'tres':
        print("El numero en letras ingresado equivale al numero: '3'")
    elif opcion2 == 'cuatro':
        print("El numero en letras ingresado equivale al numero: '4'")
    elif opcion2 == 'cinco':
        print("El numero en letras ingresado equivale al numero: '5'")
    else:
        print("El numero en letras elegido no esta en el rango solicitado. Vuelva a intentar! \n")
else:
    print("Opcion incorrecta, vuelva a ingresar opciones 1 o 2 \n")
print("Fin.")

