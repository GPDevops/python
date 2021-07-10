## LIst comprehensions

a = [1,3,5,7,9,11]
print(a)

## first solution to double elements
b=[]
b.append(2)
b.append(6)
b.append(10)
b.append(14)
b.append(18)
b.append(22)

print(b)

## mas elegante

c=[]

for x in a:
    c.append(x*2)
print(c)

## mucho mas elegante

d = [x*2 for x in a]
print(d)

## homework: create a list [1,4,9,16,25,36]

e = [1,2,3,4,5,6]           #first method
f = [x**2 for x in e]
print(f)

g = []                      #second method
for x in e:
    g.append(x**2)
print(g)

## homework create the following list [36,25,16,9,4,1]

h = [6,5,4,3,2,1]           #first solution
i = [x*x for x in h]
print(i)

j=[]                        #second solution
for x in h:
    j.append(x*x)
print(j)


for x in range(6,0,-1):     #third solution with ranges
    print(x)






