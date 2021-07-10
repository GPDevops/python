# first example
a = 2
b = 5
if a < b:
    print("a is less than b")
elif a == b:
    print("a is equal to b")
else:
    print("a is not less than b")

# second example

c = 20
d = 10
if c < d:
    print("c is less than d")
else:
    if c == d:
        print("c is equal to d")
    else:
        print("c is greater than d")

# third example

## identify bmi (body mass index = weight/height)
print("PROGRAM TO CALCULATE YOUR BMI")
name = input("Please input your name: ")
print("Hello " + name + " Please provide the following information: ")
weight = int(input("What is your weight in Kg: "))
height = float(input("What is your height in m: "))
bmi = weight / (height * height) 
if bmi < 27.8:
    print("Congratulations..Your BMI is normal and equal to: " + str(bmi))
else:
    if bmi == 27.8:
        print("No good.. Your BMI is equal to: " + str(bmi))
    else:
        print("warning.. Your BMI is equal to: " + str(bmi) + " You are in danger...")


    

        


