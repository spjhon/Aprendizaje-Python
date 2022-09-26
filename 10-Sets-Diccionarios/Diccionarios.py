# Un diccionario es un tipo de dato que almacena un conjunto de datos en formato clave > valor
# es parecido a un array asociativo o un objeto json

personas = {
    "nombre": "Victor", # Aca vemos la clave y el indice
    "apellidos": "Robles",
    "web": "victorroblesweb.es"
}

# Como acceder a estos elementos

print (personas ["Apellidos"]) # De esta forma se accede a cada uno de los indices

-----------------------
# Ahora se va a hacer un diccionario multidimencional

contactos = [
    {
        "Nombre": "Antonio",
        "Email": "antonio@antonio.com"
    },
    {
        "Nombre": "Luis",
        "Email": "luis@luis.com"
    },
    {
        "Nombre": "Salvador",
        "Email": "salvador@salvador.com" 
    }
]

print (contactos)
print (contactos [0]["Nombre"])

print ("\n Listado de contactos: ")

for contacto in contactos:
    print (f"Nombre del contacto: {contacto['Nombre']}")
    print (f"Email del contacto: {contacto['Email']}")
    print ("----------------------------------------")