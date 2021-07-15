#Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.

#makes10(9, 10) → True
#makes10(9, 9) → False
#makes10(1, 9) → True

def makes10(x,y):
    if x == 10 or y ==10:
        return True
    elif (x+y) == 10:
        return True
    else:
        return False
a = makes10(9,1)
print(a)