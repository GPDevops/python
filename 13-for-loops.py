# for loops:

# conventional way to print elements

a = ["banana", "apple", "microsoft"]
print(a[0])
print(a[1])
print(a[2])

# print using for loop

for element in a:
    print(element)

for element in a:       ## imprime 2 veces el mismo elemento
    print(element)
    print(element)

# homeworK:  sum up the elements of a list

b = [20,10,5]
total =0
for e in b:             # e = element
    total= total + e
print(total)

# rangos de numero:   1,2,3,4

c = list(range(1,5))
print(c)

# homework: print the list of numbers from 1-10

d = list(range(1,11))
print(d)

# using for loop

for e in d:
    print(e)

# sum up all numbers using for loop

total2 =0
for e in d:
    total2 += e
print(total2)

#homework: dado el siguiente rango, sumar solo los que sean pares

f = list(range(1,8))
print(f)

total3=0
for e in f:             # otra opcion: for e in range(1,8):
    if e % 2 == 0:
        total3 += e
print(total3)

# homework: sumar todos los multiplos de 3 y 5 menores de 100

g = list(range(1,100))
print(g)

total4=0
for e in range(1,100):
    if e % 3 == 0 or e % 5 == 0:
        total4 += e
print(total4)

##CWDC
##homework: create a list of my favorite fruits and using a for loop print
## I like every fruit in the list

list =["Banana", "peach", "Apple"]
for i in list:
    print("I like " + i)        #si fuera un numero se lo deberia cambiar a STR
























    




    





