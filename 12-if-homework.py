#Sistema para calcular si un alumno pasa en una materia
#con sentencias condicionales if elif
#promedio para pasar el semestre 8/10
print ("++++++++++++++++++++++++++++++++++++++++++++")
print ("Programa de calculo de aprobacion de materia")
print ("++++++++++++++++++++++++++++++++++++++++++++")
nombre_alumno = str(input("Ingrese su nombre: "))
materia = str(input("Ingrese la materia: "))
nota1 = float(input("Ingrese la nota del 1er. trimestre sobre 10: "))
nota2 = float(input("Ingrese la nota del 2do. trimestre sobre 10: "))
nota3 = float(input("Ingrese la nota del 3er. trimestre sobre 10: "))
promedio = (nota1 + nota2 + nota3)/3
#promedio = int(promedio)
if promedio >= 8:
    print("Felicitaciones! " + nombre_alumno + " Ud pasa de anio" + " su nota es: " , str(round(promedio,2)) + " sobre 10")
elif promedio < 8:
    print("Lo lamentamos! " + nombre_alumno + " Ud pierde el anio" + " su nota es: " , str(round(promedio,2)) + " sobre 10")
print("Fin.")
