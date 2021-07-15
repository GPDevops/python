#Given an int n, return True if it is within 10 of 100 or 200 
#Note: abs(num) computes the absolute value of a number.

#near_hundred(93) → True
#near_hundred(90) → True
#near_hundred(89) → False

def near_hundred(n):
    if n < 100 and n >= 90:
        return True
    elif n >= 100 and n <= 110:
        return True
    elif n < 200 and n >= 190:
        return True
    elif n >= 200 and n <= 210:
        return True
    else:
        return False
a = near_hundred(0)
print(a)


