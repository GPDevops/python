#Tipo de datos boolean
#function type transforma el tipo de dato de lo que se encuentra entre parentesis
x="microsoft"
print("El valor ingresado anteriormente es un: ", type(x))
y=4
print("El valor ingresado anteriormente es un: ", type(y))

#Comparacion de valores con salida boolean
a = 3
b = 1
if a > b:
    print("a is greater than b")
if True:
    print("a is greater than b")
boolean_value = a > b
print(boolean_value)
if boolean_value:
    print("a is greater than b")
#definiendo una funcion
def are_you_sad(is_rainy, has_umbrella):
    if is_rainy == True and has_umbrella == True:
        return True
    else:
        return False
#Lo anterior pero de otra forma
def are_you_sad(is_rainy, has_umbrella):
    if is_rainy and not has_umbrella:
        return True
    else:
        return False
#mas simplificado
def are_you_sad(is_rainy, has_umbrella):
    return is_rainy and not has_umbrella
    
a = are_you_sad(True,False)
print(a)
b = are_you_sad(False, False)
print(b)

#nueva funcion
def c_greater_than_d_plus_e(c,d,e):
    return c > d + e
f = c_greater_than_d_plus_e(3,1,1)
print(f)
g = c_greater_than_d_plus_e(3,3,1)
print(g)