# while loops

# using for loop to sum up the numbers in the range 1 to 4

total = 0
for i in range(1,5):
    total += i
print(total) 

# now using while loop and using the same range

total2 = 0
j=1
while j<5:
    total2 +=j
    j += 1
print(total2)

# while loops should be used when there is not certainty
# of how many loops requires to be done (SUMAR LOS NUM POSITIVOS)

given_list = [5,4,4,3,1,-2,-3,-5]
total3 = 0
i = 0

while given_list[i] > 0:
    total3 += given_list[i]
    i += 1
    print("Interaccion: " + str(total3))
print(total3)

# another way

given_list = [5,4,4,3,1]
total4 =0
i =0
while i< len(given_list) and given_list[i] >0:
    total4 += given_list[i]
    i += 1
print(total4)

# using for and break to solve the same issue

given_list2 = [5,4,4,3,1,-2,-3,-5]
total5=0
for element in given_list2:
    if element <=0:
        break
    total5 +=element
    print(total5)

# homework: dada la lista sumar solo los negativos
# Con for
given_list3 = [5,4,4,3,1,-2,-3,-5,-7]

total6 =0
for element in given_list3:
    if element < 0:
        total6 += element
print(total6)

#Con while
given_list4 = [5,4,4,3,1,-2,-3,-5,-7]
total7 =0
i=0
while i< len(given_list4):
    if given_list4[i] < 0:
        total7 += given_list4[i]
    i += 1
print(total7)

##CWDC
##homework: create a list of my favorite fruits and using a for/while loop print
## I like every fruit in the list

list =["Banana", "peach", "Apple"]
print(list[0])
for i in list:
    print("I like " + i)


list2 =["orange", "apple", "banana", "mango"]
cont = 0
while cont < len(list2):
    print("I like " + list2[cont] + ".")
    cont += 1

##homework: create a dictionary - 4 names (key) and ages (values) of people
## loop which prints. eg. Sam is 7 years

dict = {}
dict["Sofi"] = 52
dict["juanito"] = 31
dict["Estebita"] = 28
dict["Oscar"] = 25

for key, value in dict.items():
    print(key + " is " + str(value) + " years")





    

























    




    





