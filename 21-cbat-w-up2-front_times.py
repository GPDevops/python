#Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars,
#or whatever is there if the string is less than length 3. Return n copies of the front;

#front_times('Chocolate', 2) → 'ChoCho'
#front_times('Chocolate', 3) → 'ChoChoCho'
#front_times('Abc', 3) → 'AbcAbcAbc'

def front_times(str, n):
    if len(str) < 3:
        return str*n
    else:
        front = str[:3]
        front3 = front*n
        return front3
a = front_times("abc",4)
print(a)

# otra solucion....mas tecnica

def front_times4(str, n):
  front_len = 3
  if front_len > len(str):
    front_len = len(str)
  front = str[:front_len]
  print(front)
  result = ""
  for i in range(n):
    result = result + front
  return result

b = front_times4("Gonzalo", 4)
print(b)