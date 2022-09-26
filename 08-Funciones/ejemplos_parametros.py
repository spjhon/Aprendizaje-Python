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


#Ejemplo, las tablas de multiplicar pero con funciones y parametros

def tabla(numero):
    print(f"Tabla de multiplicar del numero: {numero}")
    
    for contador in range (11):
        resultado = numero*contador
        print(f"{numero} x {contador} = {resultado}")
    
tabla(3)


# Ejemplo con PARAMETROS OPCIONALES

def getEmpleado (nombre, DNI = ""):
    print ("EMPLEADO")
    print (f"Nombre: {nombre}")
    
    if DNI != "":
        print (f"DNI: {DNI}")

getEmpleado("Juan Camilo", input("Ingrese DNI: "))



# Funcion de generar una calculadora pero no imprimir sino devolver un string y luego imprimir

# Un return es que se logre extrear datos de una funcion

def calculadora (numero1, numero2, basicas = False):
    
    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    division = numero1 / numero2
    
    cadena = ""
    
    if basicas == True:
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
    else:
        cadena += "Multiplicacion: " + str(multi)
        cadena += "\n"
        cadena += "Division: " + str(division)

    return cadena

print (calculadora (5,5))



#Funciones dentro de otras funciones

def getNombre (nombre):
    texto = f"El nombre es: {nombre} JAJAJJA"
    return texto

def getApellido (apellidos):
    texto = f"El apellido es: {apellidos} JAJAJJA"
    return texto

def devuelveTodo (nombre, apellidos):
    texto = getNombre(nombre) + " " + getApellido(apellidos)
    return texto

print (devuelveTodo ("Victor", "Robles"))


# Una funcion LAMBDA es anonima, es una funcion sin nombre y no hace falta el def.
# Es o fue disenada para tareas pequenas pero repetitivas y solo se limita a UNA LINEA

dime_el_year = lambda year: f"Estamos en el ano: {year+2}"

print (dime_el_year(2034))