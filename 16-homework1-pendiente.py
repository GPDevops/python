# homework: imprimir los primeros 10 numeros primos 
## eg, 2,3,5,7

#numero primo = divisible por si mismo y para la unidad unicamente


       
numberofprimes =0
number =2
while numberofprimes < 10:
    isprime =True
    for i in range(2, number):
        if number % i ==0:
             isprime =False
    if isprime == True:
        print(number)
        numberofprimes +=1
    number +=1

    
     

    


    

























    




    





