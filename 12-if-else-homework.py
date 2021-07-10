## Calcular si una persona ha pasado el semestre ingresando sus notas

print("PROGRAMA PARA CALCULAR SI UN ESTUDINATE HA PASADO EL SEMESTRE")

nombre = input("Por favor ingresar su nombre: ")
print("Ingresar las notas con valor maximo 10")
algebra = float(input("Por favor ingresar la nota de algebra: "))
fisica = float(input("Por favor ingresar la nota de fisica: "))
geometria = float(input("Por favor ingresar la nota de geometria: "))
quimica = float(input("Por favor ingresar la nota de quimica: "))

calculo = (algebra + fisica + geometria + quimica)/4

if calculo <=8:
    print("Lo sentimos, " + nombre + " Su promedio es: " + str(calculo))
    print("No aprueba el semestre")
else:
    print("Felicitaciones!!, " + nombre + " Su promedio es: " + str(calculo))
    print("Aprueba el semestre")
