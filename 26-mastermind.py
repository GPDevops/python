### mastermind challenge

## manejar conexion al cgi
import cgi
form = cgi.FieldStorage()

if "name" in form:
    print(form.getvalue("name"))
else:
    print("noname")

print("<h1>Mastermind</h1>")
