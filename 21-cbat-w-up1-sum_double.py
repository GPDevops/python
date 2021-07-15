#Given two int values, return their sum. Unless the two values are the same, 
#then return double their sum.

#sum_double(1, 2) → 3
#sum_double(3, 2) → 5
#sum_double(2, 2) → 8

def sum_double(a,b):
    if a%b == 0 and b%a == 0:
        a = a**2
        b = b**2
        return a + b
    else:
        return False
f = sum_double(5,5)
print(f)