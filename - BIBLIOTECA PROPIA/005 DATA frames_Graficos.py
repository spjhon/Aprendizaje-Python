# Se utiliza la libreria pandas osea NUMPY
# Con data frames se puede trabajar desde cualquier frame CSV, XLS, PARQUET, HTML, HDF5, JSON, GBQ, SQL

# Toda columna tiene un valor (column) y toda fila tiene un indice (row)

# Ejemplo diminuto de un DATAFRAME

import pandas as pd
# Crear un data frame con las series que se vayan creando
s = pd.Series(["Matematicas", "Espanol", "Ingesl", "Programacion"]) # Se indican los datos que van alli en ese momento
# Se esta crando el dataframe con datos ingresados desde le mismo python

print (s)
# Con esto se puede crear una matriz rapidamente sin necesidad de ciclos como for para recorrer el dataframe
# La idea de los dataframe es que extraiga informacion de un archivo


# Un diccionario es como una especie de lista de listas, se puede recoger varios datos y no se esta condicionado a un solo objeto
# Los diccionarios estan compuestos por una clave y los valores, los valores van despues de los dos puntos
# y se debe colocar cola al final


# Estructura de datos son diccionarios

diccionario =  {
    "clave": [5,6,67,6,6,9],
    "kfdslk": ["Valores", "abcdef", "ghijk"]
}
--------------------------------------------------
# Ahora se va a hacer desde excel

import pandas as pd
# Para trabajar datos desde excel se necesita otra libreir

path = "Datos.xlsx"
# io quiere decir entrada input-outpu, el segundo parametro es la hoja
# datos1 = pd.read_excel(path)
datos = pd.read_excel(io = "Datos.xlsx", sheet_name = "Hoja1")
 
print(datos)

------------------------------------------------------

# Con la libreria matplotlib se pueden crear graficos 2D, configurar y desarrollar graficos estadisticos
# Ahora se va a trabajar en como crear graficos en python

import matplotlib.pylab as plt
# El subplots es un metodo para graficas y esas dos variables se les asigna la libreria
flig, ax = plt.subplots ()

ax.plot ([1,2,3,4], [1,2,0,0.5])

#Ahora se va a mostrar el grafico
# Grafico de un diagrama de lineas

plt.show ()

------------------------------------------------------------

import matplotlib.pylab as plt
# Ahora se va a crear un grafico de barras verticales

fig, ax = plt.subplots ()

x = [1,2,3]
y = [3,2,1]

ax.bar (x, y)

plt.show ()

----------------------------------------------
# Dibujado de barras estadisticas horizontales

import matplotlib.pylab as plt
# Ahora se va a crear un grafico de barras verticales

fig, ax = plt.subplots ()

x = [1,2,3]
y = [3,2,1]

# Agregandole una h al bar y se hacen horizontales las barras
ax.barh (x, y)

plt.show ()

-----------------------------------------

# Dibujado tipo torta con la libreria matplotlib

import matplotlib.pylab as plt

fig, ax = plt.subplots()

# Vamos a crear los putnos que va a llevar el grafico
# Esto es un grafico de torta o PIE
ax.pie([5,4,3,2,7])
plt.show()

# Esto se le llaman graficos estaticos no poseen etiquetas o elementos puntuales

---------------------------------------

# Dibujado con listas y diccionarios

import matplotlib.pylab as plt

fig, ax = plt.subplots()

# Vamos a crear una lista y dos diccionarios

dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

# Ahora un diccionario que lleve temperatura des ciudades

temp_diaria = {
    # Acordarse que debe de llevar clave y valor
    "Barranquilla": [25, 27.3, 29, 22.3, 28.8, 30, 32],
    "Chiquinquira": [15, 18, 13, 12.3, 10, 20, 16]
}

# Ahora vamos a agregar datos a los axiomas
# Ojo con temp_diaria ya que es un diccionario, el tab indica un color predeterminado en la libreria
# Ademas se le pueden agregar simbolos extra a los datos presentados en la tabla
ax.plot(dias, temp_diaria["Barranquilla"],color = 'tab:purple',marker="^")
ax.plot(dias, temp_diaria["Chiquinquira"],color = 'tab:green',marker="^")
plt.show()

---------------------------------------------

# Dibujado con listas y diccionarios

import matplotlib.pylab as plt

fig, ax = plt.subplots()

# Vamos a crear una lista y dos diccionarios

dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

# Ahora un diccionario que lleve temperatura des ciudades

temp_diaria = {
    # Acordarse que debe de llevar clave y valor
    "Barranquilla": [25, 27.3, 29, 22.3, 28.8, 30, 32],
    "Chiquinquira": [15, 18, 13, 12.3, 10, 20, 16]
}

# Ahora vamos a agregar datos a los axiomas
# Ojo con temp_diaria ya que es un diccionario, el tab indica un color predeterminado en la libreria
# Ademas se le pueden agregar simbolos extra a los datos presentados en la tabla
ax.plot(dias, temp_diaria["Barranquilla"],color = 'tab:purple',marker="^")
ax.plot(dias, temp_diaria["Chiquinquira"],color = 'tab:green',marker="^")
# Loc es localizacion, fuente es font
ax.set_title ("ESTE ES EL TITULO CON UN TIPO DE LETRA PREDETERMINADO", loc = "Left", fontdict={'fontsize':16, 'fontweight':'bold', 'color':'blue'})
# Ahora agregarle leyendas a los graficos
ax.set_ylabel ('Temperadura en grados C')
ax.set_xlabel ('Dias de la semana')

plt.show()

# Ahora se le va a agregar el titulo

------------------------------------------------
# Parte grafica de Phyton con Tkinter
# Con esto se puede hacer aplicaciones para el sistema operativo y multiplataforma (cualquier sistema operativo, linux, windows, mac)
# Biblioteca de codigo abierto escrito en c y se adapto para trabajar con python que tambien fue creado en C
# CONSEJO, SIEMPRE UTILIZE FUNCIONES PARA MODULAR EL CODIGO
import tkinter as tk # Incorporar la libreria tkinter
# Cuando se importan librerias, se pueden incorporar libreriras completas o solo modulos
# Para este ejercicio se importa un modulo especifico para la crearion del entorno donde va a interactuar el usuario

from tkinter import ttk # Este modulo le permite trabajar directamente con elementos como cajas de texto, labls, etc.
# si o si debe de tener inicio y final
# Para este ejercicio vamos a crear un convertidor de temperatura
def convertir_temp (): # La idea de esta funcion es que coja lo que hay en la caja de texto y lo convierta
    temp=float(caja_texto_temperatura.get())
    temp_convertida = temp*1.8+32 # Aqui se hace la conversion y se guarda en una variable
    etiqueta_resultado.config (text=f"La temperatrua en Farengeight es: {temp_convertida}")
    etiqueta_resultado.place (x=20, y=130)
# Inicio, crear una variable a la cual se le va a incorporar esta libreria

interfaz = tk.Tk()
interfaz.title ("VENTANA DE PRUEBA") # Se define el titutlo
interfaz.config (width=400, height=300) # Definimos el alto y el ancho de la interfaz, la unidad de medida es pixeles
interfaz.resizable (False, False) # Deja que el usuario modifique la ventana con el 0, 0 se esta diciendo que no deje cambiar el tamano de la ventana
etiqueta_temperatura_inicial = ttk.Label (text = "INGRESE TEMPERATURA") # Etiqueda de donde el usuario va a ingresar los datos
etiqueta_temperatura_inicial.place (x=20, y=20) # Posicion de la etiqueta
caja_texto_temperatura=ttk.Entry () # Caja de texto donde se va a ingresar la informacion
caja_texto_temperatura.place (x=20, y=50)
boton_convertir = ttk.Button (text = "CONVERTIR", command=convertir_temp) # Se le esta diciendo que cuando el usuario le de al boton, se va a ejecutar la fucnion
boton_convertir.place (x=20, y=80)
etiqueta_resultado = ttk.Label (text="La temperatura que ingreso convertida en Farengeight es: ")
etiqueta_resultado.place (x=20, y=110)
# Final
interfaz.mainloop() # Esto es como un ciclo repetitivo, osea que cuando se ejecute la ventana 


