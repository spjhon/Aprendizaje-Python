# Listas multidimencionales
# Esto es una lista de listas
print("\n**************LISTA DE CONTACTOS***********")

contactos = [
    [
      "Antonio",
      "antonio@antonio.com"  
    ],
    [
        "Luis",
        "luis@luis.com"
    ], 
    [
        "Salvador",
        "salvador@salvador.com"
    ]  
]

print(contactos)

# Otra forma de escribirlo es

contactos_horizontal = [["Antonio", "antonio@antonio.com"], ["Luis", "luis@luis.com"], ["Salvador", "salvador@salvador.com"]]
# print (contactos_horizontal)

# si se quiere imprimir solo el email de luis
print (contactos[1][1])

# una forma de recorrer las listas dentro de las listas

for a in contactos:
    print(a[0])
    
for a in contactos: # Una forma de recorrer todas las listas pero de forma manual
    print(a[0])
    print(a[1])
                
for a in contactos: # Otra forma de recorrer las listas dentro de listas
    for b in a:
        print(b)