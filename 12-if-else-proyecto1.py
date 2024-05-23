#la compania Rappi, solicita un sistema que determine los dias de vacaciones a los que tiene
#derecho un trabajador, tomando en cuenta las siguientes caracteristicas:
#existen 3 departamentos dentro d ela compania con sus respectivas claves:
#1. Departamento de atencion al cliente: Clave1
# - Trabajadores con 1 anio de servicio, reciben: 6 dias de vacaciones.
# - Trabajadores con 2 a 6 anios de servicio, reciben: 14 dias de vacaciones.
# - Trabajadores a partir de 7 anios de servicio, reciben 20 dias de vacaciones.
#2. Departamento de logistica: Clave2
# - Trabajadores con 1 anio de servicio, reciben: 7 dias de vacaciones.
# - Trabajadores con 2 a 6 anios de servicio, reciben: 15 dias de vacaciones.
# - Trabajadores a partir de 7 anios de servicio, reciben 22 dias de vacaciones.
#3. Gerencia: Clave3
# - Trabajadores con 1 anio de servicio, reciben: 10 dias de vacaciones.
# - Trabajadores con 2 a 6 anios de servicio, reciben: 20 dias de vacaciones.
# - Trabajadores a partir de 7 anios de servicio, reciben 30 dias de vacaciones.
# Requerimientos:
# - El sistema debe solicitar el "Nombre", "Clave del departamento" y "antiguedad del trabajador desde teclado
# - Posteriormente, El sistema debe mostrar un mensaje en pantalla, que contenga el "Nombre del Trabajador",
#   y los dias de vacaciones a los que tiene derecho.
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("programa para determinar los dias de vacaciones de un trabajador de acuerdo a sus anios de trabajo")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
while True:
    nombre = input("Por favor ingrese su nombre: ")
    if nombre.isalpha():
        print(f"¡Hola, {nombre}! Has ingresado un nombre válido.")
        break
    else:
        print("El nombre debe contener solo letras. Inténtalo nuevamente.")

while True:
    clave = int(input("Por favor ingresar su clave de departamento: "))
    if clave < 4:
        print("Opcion de clave valida")
        break
    else:
        print("Opcion de clave no valida")


anios = float(input("Por favor ingresar los anios de antiguedad: "))   
if clave == 1:
    if anios >= 1 and anios < 2:
                print("Sr, ", nombre, "Ud tiene derecho a: 6 dias de vacaciones")
    elif anios >= 2 and anios < 7:
                    print("Sr, ", nombre, "Ud tiene derecho a: 14 dias de vacaciones")
    elif anios >= 7:
                    print("Sr, ", nombre, "Ud tiene derecho a: 20 dias de vacaciones")
    else:
                    print("Opcion de anios no valida. Ud no tiene vacaciones")
elif clave == 2:
    if anios >= 1 and anios < 2:
        print("Sr, ", nombre, "Ud tiene derecho a: 7 dias de vacaciones")
    elif anios >= 2 and anios < 7:
        print("Sr, ", nombre, "Ud tiene derecho a: 15 dias de vacaciones")
    elif anios >= 7:
        print("Sr, ", nombre, "Ud tiene derecho a: 22 dias de vacaciones")
    else:
        print("Opcion de anios no valida. Ud no tiene vacaciones")    
elif clave == 3:
    if anios >= 1 and anios < 2:
        print("Sr, ", nombre, "Ud tiene derecho a: 10 dias de vacaciones")
    elif anios >= 2 and anios < 7:
        print("Sr, ", nombre, "Ud tiene derecho a: 20 dias de vacaciones")
    elif anios >= 7:
        print("Sr, ", nombre, "Ud tiene derecho a: 30 dias de vacaciones")
    else:
        print("Opcion de anios no valida. Ud no tiene vacaciones") 
else:
    print("Opcion de clave no valida.") 