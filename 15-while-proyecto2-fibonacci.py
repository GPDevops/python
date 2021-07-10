#desarrollar un programa que imprima en pantalla la sucesion de Fibonacci 
#desde el numero 0 hasta el numero 1597, de manera horizontal
#requerimientos:
# - El programa debera tener maximo 7 lineas de codigo
# 

num_ant, num_sig = 0,1
while num_sig <= 1597:
    print(num_ant, num_sig, end=" ")
    num_ant = num_ant + num_sig
    num_sig = num_ant + num_sig


