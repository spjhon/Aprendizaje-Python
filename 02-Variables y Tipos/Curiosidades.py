# Curiosidades de las variables
# No se pueden utilizar comas ni tildes ni guiones

texto1 = "Master"
texto2 = " en Python"

Texto_unido = texto1 + texto2
print(Texto_unido)

# Para que aparezcan las comillas en el string
# una forma es utilizando el \, otra forma es utilizando comillas simpes ''
print ("texto \"con comillas\" ")
print ("asi 'se utilizan comillas simples'")
# para meterle un SALTO DE LINEA o un ENTER se utiliza un \n
#para meterle una tabulacion se utiliza \t
print ("Esta es una linea \nEsta es otra linea")
print ("antes de tabulacion \tDespues de tabulacion")
# con \r reemplaza letra a letra lo que esta atras del simbolo con lo que esta delante
# del simbolo y lo que sobre se deja
print ("Esto no se deberia ver \r     ")

# CASTING para declarar una variable
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# Obtener el tipo de variable que es
x = 5
y = "John"
print(type(x))
print(type(y))

# DESEMPAQUETAR una lista en variables

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Asi se guarda una cadena larga de caracteres en una variable
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Un string es solo una cadena de array, asi se puede imprimir un punto en especifico
a = "Hello, World!"
print(a[1])

# Esta es una forma de checkear un string
txt = "The best things in life are free!"
print("free" in txt)

# Una busqueda utilizando un loop
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")