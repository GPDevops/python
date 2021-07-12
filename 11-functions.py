# functions: it is a collection of instructions/collection of code
"""
def function1():
    print("This is part of function1")
    print("This is part of function1...2")
print("this is outside of the function")

function1()     ##llamar a la funcion

# a mapping
# x can be an input or an argument

def function2(x):
    return 2*x
a = function2(3)    #return value or output
print(a)

b = function2(4)
print(b)

c = function2(5)
print(c)

# functions with two arguments

def function3(x,y):
    return x+y
e = function3(1,2)
print(e)

# combine of functions

def function4(x):
    print(x)
    print("still in this function")
    return 3*x
f = function4(4)
print(f)

# BMI CALCULATOR

name1       = input ("Ingrese el nombre de la Persona: ")
height_m1   = float(input("Ingrese su altura en metros: "))
weight_kg1  = float(input("Ingrese su peso en kilogramos: "))

name2 = "YK's sister"
height_m2 = 1.8
weight_kg2 = 70

name3 = "YK's brother"
height_m3 = 2.4
weight_kg3 = 160

def bmi_calculator(name, height_m, weight_kg):
    bmi = weight_kg / (height_m ** 2)
    print("bmi: ")
    print(bmi)
    if bmi < 27.8:
        return name + " is not overweight"
    else:
        return name + " is overweight"

result1 = bmi_calculator(name1, height_m1, weight_kg1)

result2 = bmi_calculator(name2, height_m2, weight_kg2)
result3 = bmi_calculator(name3, height_m3, weight_kg3)
print(result1)

print(result2)
print(result3)


# FUNCTION TO CONVERT KM TO MILES

def convert(miles):
    return 1.6 * miles
miles = int(input("Ingrese el valor de millas a convertir: "))
calculo = convert(miles)
print("El valor de millas ingresado equivale a: " + str(calculo) + "kms")

# function to convert km to miles and viceversa

print("++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Programa para convertir millas a kms y viceversa")
print("++++++++++++++++++++++++++++++++++++++++++++++++++")
def convert1(miles):
    return 1.6 * miles

def convert2(kms):
    return  0.625 * kms

dato = int(input("selecione la opcion:  1 para miles, 2 para Kms: "))
if dato == 1:
    print("Su eleccion es: " + str(dato) + " Conversion de millas a Kms")
    miles = float(input("Ingrese el valor en millas a convertir: "))
    calculo = convert1(miles)
    print("El valor de millas ingresado equivale a: " + str(calculo) + " kms")
else:
    print("Su eleccion es: " + str(dato) + " Conversion de Kms a millas")
    kms = float(input("Ingrese el valor en kms a convertir: "))
    calculo = convert2(kms)
    print("El valor de kms ingresado equivale a: " + str(calculo) + " miles")

##CWDC
##create a function highestCommonFactor which returns
##the highest number that divides into two other numbers exactly
"""
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Programa para calcular maximum comun divisor MCD entre 2 numeros")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

def maximumCommonFactor(x,y):
    for i in range(1,x+1):
        if x%i ==0 and y%i == 0:
            hcf = i
    return hcf
     
fact1 = int(input("Ingrese el numero x: "))
fact2 = int(input("Ingrese el numero y: "))
print ("El MCD es: " + str(maximumCommonFactor(fact1,fact2)))

"""""
a=5
b=6
def addTwoNumbers():
    return a+b
print(addTwoNumbers())
"""
"""
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Programa para calcular minimo comun multiplo MCM entre 2 numeros")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

num1 = int(input("Ingresa numero A: "))
num2 = int(input("Ingresa numero B: "))

A = max(num1,num2)
B = min(num1,num2)
print(A)
print(B)

##def minimumCommonFactor(x,y):
while B !=0:
    mcd =   B
    B   =   A%B
    A   =   mcd
    print(A,B)
mcm = (num1*num2) // mcd
     
     
print ("El MCD de {0} y {1} es {2}". format(num1,num2, mcd))
print ("El MCM de {0} y {1} es {2}". format(num1,num2, mcm))
"""