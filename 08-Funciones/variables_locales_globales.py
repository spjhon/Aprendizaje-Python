# Una variable local es aquella que se define dentro de la funcion y no puede
#utilizarse dentro de la funcion

#Las globales estan declaradas afuera de las funciones y pueden ser utilizadas dentro 
#y fuera de las funciones

#Variable global

frase = "Ni los genios son gan tenios ni los mediocres tan mediocres"

print(frase)

def holaMundo():
    frase = "Dentro de la funcion"
    print (frase)
    
holaMundo()