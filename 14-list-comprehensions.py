a = [1,3,5,7,9,11]
# queremos tener una lista como esta -> [2,6,10,14,18,22]
# vamos a usar la funcion  .append()
b =[]
b.append(10)
b.append(20)
print(b)
#para logra lo indicado debemos crear una lista vacia y con el for crear los elementos indicados.
c = []
for x in a:
    c.append(x*2)
print(c)
# ahora una forma simplificada de hacer lo mismo. mas elegante
d = [x*2 for x in a]
print(d)
# nuevo ejercicio
#crear un alista [1,4,9,16,25,36]
#1ra forma:
e =[]
e.append(1)
e.append(4)
e.append(9)
e.append(16)
e.append(25)
e.append(36)
print(e)
#2da.solucion
f = []
for x in range(1,7):
    f.append(x**2)
print(f)
#3ra.solucion
g = []
g = [x**2 for x in range(1,7)]
print(g)
#nuevo ejercicio
# crear la siguiente lista [36,25,16,9,4,1]
for x in range(6,0,-1):
    print(x)
h = []
for x in range(6,0,-1):
    h.append(x**2)
print(h)
#otra solucion utilizando list comprehensions
i = [x**2 for x in range(6,0,-1)]
print(i)

