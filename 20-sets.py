## sets in phyton
## a set is atype of data that stores a set of things
## a set of unique things
## {1,3} <- 3
## ->{1,3}

a =set()
print(a)

a.add(1)
print(a)

a.add(2)
print(a)

a.add(2)        #no aniade porque el elemnto ya esta anteriormente ingresado
print(a)

for x in a:     #hace lo mismo de lo anterior
    print(x)

## eliminar duplicados de una lista

given_list1 = [1,1,2,4,2]

new_set1 = set()
for x in given_list1:
    new_set1.add(x)
print(new_set1)

## como convertir un set a una lista
# partimos del set {1,2,4}

new_list1 = list()
for x in new_set1:
    new_list1.append(x)
print(new_list1)

## se puede aniadir strings pero tomar en cuenta los siguiente

b = set()
b.add('apple')
b.add('banana')
b.add(1)
print(b)            #el resultado es {1,'banana', 'apple'} al reves de lo que se aniade en las listas


# homework: dada la lista [1,3,4,1,3], sumar los elementos, pero no los repetidos

given_list2 = [1,3,4,1,3]       #solucion1
new_set2 = set()
for x in given_list2:
    new_set2.add(x)
print(new_set2)

new_list2 = list()
for x in new_set2:
    new_list2.append(x)
print(new_list2)

suma = 0
for x in new_list2:
    suma += x
print(suma)

## otra solucion

given_list3 = [1,3,4,1,3]       #solucion2 sin necesidad de convertir set a list
new_set3 = set()
for x in given_list3:
    new_set3.add(x)
print(new_set3)

suma = 0
for x in new_set3:
    suma += x
print(suma)  




    
    




























