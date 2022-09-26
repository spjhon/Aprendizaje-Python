#Una funcion es un conjunto de instrucciones agrupadas bajo un nombre concreto y que pueden reutilizarsen
#cuantas veces se quieran

# def nombreDeMiFuncion(parametros):
#   Conjunto de instrucciones

#Y para invocar la funcion
#nombreDeMiFuncion(mi_parametro)

#PARAMETRO: 

#Ejemplo 1

print("Ejemplo 1")

def muestraNombres():
    print("Juan")
    print("Paco")
    print("Fancisco")
    print("Victor")
    print("\n")
    
# Invocar funcion

muestraNombres()

#PARAMETROS
print("Ejemplo 1")

def mostratTunombre():
    print("")

#PARAMETROS
print("Ejemplo 1")

# Con los parametros lo que se hace es que se esta ingresando un dato
#a que se procese de acuerdo al codigo dentro de la funcion, no se necesitan crear variables en otro lado
#solo en la funcion, asi cuando se invoque se lleva el dato directo a la funcion sin que tenga que paras por variables

def mostratTunombre(variablenombre, edad):
    print(variablenombre)
    if edad >= 18:
        print ("Es mayor de edad")
    else:
        print ("Es MENOR de edad")
            

variable_externa_para_inseratar_en_la_funcion = input ("Introduce tu nombre: ")
edad_variable_externa = int(input("Ingrese la edad: "))
mostratTunombre(variable_externa_para_inseratar_en_la_funcion, edad_variable_externa)