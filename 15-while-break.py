#ejemplo para break
print("while con la sentencia break \n")
contador = 0
while contador < 10:
    contador += 1
    if contador == 5:
        break
    print("Valor actual de la variable: ", contador)
print("Fin del programa, la sentencia break se ha ejecutado")

#ejemplo para continue
print(" \n while con la sentencia continue \n")
contador = 0
while contador < 10:
    contador += 1
    if contador == 5:
        continue
    print("Valor actual de la variable: ", contador)
print("Fin del programa, la sentencia continue se ha ejecutado, por lo que no se imprime la linea 5")