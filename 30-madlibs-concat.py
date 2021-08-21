#string concatenation (aka how to put strings together)
#suppse you want to create a string that says "subscribe to ______"
#youtuber = "Gponce"#some string variable
# three methods to do this
#print("subscribe to " + youtuber)
#print("subscribe to {}".format(youtuber))
#print(f"subscribe to {youtuber}")

nombre1 = input("Ingrese un Nombre: ")
expresion = input("Ingrese una expresion: ")
adjetivo = input("Ingrese un adjetivo: ")
nombre2 = input("Ingrese un nombre: ")

madlibs = f"Este es un ejemplo de concatenacion de frases!, en los cuales ingresamos por teclado \
varias expresiones, por ejemplo: {nombre1} esta enamorado/a de {nombre2}! y le desea {adjetivo} porque es un chico/a {expresion}"

print(madlibs)