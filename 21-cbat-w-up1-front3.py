#Given a string, we'll say that the front is the first 3 chars of the string. 
#If the string length is less than 3, the front is whatever is there. 
#Return a new string which is 3 copies of the front.

#front3('Java') → 'JavJavJav'
#front3('Chocolate') → 'ChoChoCho'
#front3('abc') → 'abcabcabc'

def front3(str):
    if len(str) <= 3:
        return str+str+str
    elif len(str) > 3:
        return str[0]+str[1]+str[2]+str[0]+str[1]+str[2]+str[0]+str[1]+str[2] 

a = front3("Gonzalo")
print(a)

# otra solucion. mas tecnica

def front4(str):
  # Figure the end of the front
  front_end = 3
  if len(str) < front_end:
    front_end = len(str)
  front = str[:front_end]
  return front + front + front

b = front4("Hola") 
print(b)
  
  # Could omit the if logic, and write simply front = str[:3]
  # since the slice is silent about out-of-bounds conditions.