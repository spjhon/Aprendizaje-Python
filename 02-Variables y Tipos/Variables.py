"""
Una varible es un contenedor de informacion
que dentro guardara un dato, se pueden crear 
muchas variables y cada una contener un dato distinto.
"""
# Crear variables e imprimirlas
texto = "Máster en Python"
texto2 = "Por Udemy"
numero = 45
print(texto)
print(texto2)
print(numero)

# Cambio del contenido de las variables e imprimirlas
texto = "Cambio de texto"
texto2 = "Nuevo cambio de texto"
numero = 89.6
print(texto)
print(texto2)
print(numero)

# Ahora se va mostrar la CONCATENACION
nombre = "Juan "
apellido = "Patino "
web = f" Esta en internet + {nombre}"

print(nombre + apellido + "--" + web)
print(f"Vamos a imprimir {nombre}, {web}, y el apellido {apellido}")

# Esta es otra forma de CONCATENAR
print("Hola este es mi nombre {} {} y esta es la web {}".format(nombre, apellido, web))

# O la forma sencilla, directamente las variables
print (nombre, apellido, web)
