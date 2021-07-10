## codingbat.com
## Given a string, return a string where for every char in the original,
## there are two chars.


##double_char('The') → 'TThhee'
##double_char('AAbb') → 'AAAAbbbb'
##double_char('Hi-There') → 'HHii--TThheerree'

given = "The"
new = []
for e in given:
    new += e
    new += e
print(new)

def double_char(str):    
    to_return = ""
    for c in str:
        to_return += c*2
    return to_return
    






















    
    




























