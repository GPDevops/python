# lists: list of data such as strings, integers such as arrays

a = [3,10,-1]
print(a)

# adding elements to the list

a.append(1)
print(a)

a.append("hello")
print(a)

a.append([1,2])
print(a)


# deleting items from the list

a.pop()         #borra el ultimo item
print(a)

#retriving one item from the list

print(a[0])
print(a[4])

# changing the content of specific value

a[0] = 100      #first we have to assign the new value
print(a)

# homework. swap values from a[0] to a[2] and viceversa

a = ["banana","apple", "microsoft"]
print(a)

temp = a[0]
print(temp)         #temp=banana
a[0] = a[2]         # a[0]= microsoft
print(a[0])
a[2] = temp         # a[2]= banana
print(a)

##otra solucion

a[0], a[2] = a[2], a[0]
print(a)

###CWDC

myTuple =(1,2,3,4)
print(myTuple)

myTuple[0] = 10          ##tuplas son read only
print(myTuple)          ###no es posible actualizar ls tuplas

















    




    





