#Reto 03, Inventario sucursales
# Hola, intentare explicar lo que hice en este ejercicio, demas que habra una forma mas corta y hasta sencilla de hacerlo
# pero de esta forma funciono, muchos trucos no fueron ensenados en clase y los busque por google.

#lo que hice inicialmente fue hacer un programa que medio cumpliera las reglas, luego fui adaptando las reglas de entrada
# y salida para ajustarsen al ejemplo 1 del documento reto3-3.

# Para los que no entienden como probar el programa con los ejemplos del documento
#En el ejemplo 1 del documento dice 3 5, esto es una entrada que dice que se digita en 3, se le da barra espaciadora y luego se digita el 5 y luego se le da enter, esta entrada TIENE de ser str()
#En la siguiente linea dice 941, esto es una entrada que dice que se digita 941 y se da enter
#Mas abajo dice 1 87 82, eso es una entrada que dice que se digita 1, luego se le da espacio, luego se digita el 87, luego se le da espacio y finalmente se digita 82 y se da enter
# De esta forma se ingresan todos los datos del ejemplo 1 en orden como se muestra en el documento entonces toca adaptar el programa para que las entradas sean asi

#Lo que diga SE TIENE QUE BORRAR son los print que se deben de borrar antes de montar el archivo en la plataforma y no hayan errores

sucursales = int() # Esta variable la cree entera ya que aca se van a guardar el numero de sucursales
totalpacientes = int() # Esta variable la cree entera ya que aca se van a guardar el numero total de pacientes
medicamento = list() # Esta variable la cree en forma de lista ya que se van a guardar varias entradas de medicamento por medio de un ciclo for de acuerdo a la cantidad de sucursales que se ingresen
existencias_iniciales = list() # Esta varible la cree para guardar una lista de los medicamentos que se ingresaron para al final calcular el porcentaje ya que medicamentos va a ser modificada a medida que se le resten medicamentos
informacion_inicial = str() #Esta variable la cree para ingresar los datos de acuerdo a como se exige en el reto (que se ingresa la cantidad de sucursales y en el mismo renglon con un espacio de separacion se ingresa la cantidad de pacientes) y que luego toca separar a cada elemento (sucursales y totalpacientes) en su propia variable para poder trabajar con ellas
informacion_inicial_pacientes = str() # Esta variable fue creada al igual que la anterior con el fin de guardar la info que ingresa junta en la misma linea (sucursal del paciente, datos de la presion diatolica y sistolica) con un espacio de separacion entre ellos
informacion_inicial_pacientes_acumulado = str() # Esta variable la cree para juntar en una sola variable todos los datos de los pacientes (sucursal del paciente, datos de la presion diatolica y sistolica) de forma concatenada para trabajar con esta variable mas adelante

print("Por favor ingrese el numero de sucursales seguido del numero de pacientes totales:") # SE TIENE QUE BORRAR, este print es para orientar al usuario, SE DEBE DE BORRAR AL MOMENTO DE MONTARLO EN LA PLATAFORMA
informacion_inicial = input() #Se pide la primera linea de codigo a ingresar (cantidad de sucursales y cantidad de pacientes totales) separados por un espacio.
informacion_inicial = informacion_inicial.split(" ") #Aqui lo que hago es convertir la lista de caracteres que hay dentro de la variable en una lista.

for o in range (0, 1): # Con este rango lo unico que hago es meter en la variable sucursales el primer item de la lista informacion_inicial que corresponde a la cantidad de sucursales
    sucursales = int(informacion_inicial[o]) #Aqui le digo que almacene en la variable sucursales con un tipo de dato int la poscicion 0 de la lista informacion_inicial
    totalpacientes = int(informacion_inicial[o+1])# Aqui le digo que almacene en la variable totalpacientes almancene el item en la posicion 1 de la lista informacion_inicial
    break # Este ciclo solo da una vuelta ya que es solo para lograr separa en sus respectivas variables la informacion que muy inconvenientemente es obiligada a ser ingresada sobre la cantidad de sucursales y la cantidad de pacientes de acuerdo al reto3

while True: # Con esta condicion estoy diciendo que mientras la variable sucursales sea menor que 1 se siga solicitando que se actualice la variable hasta que se ingrese un numero mayor a 1 (este es un requisito que se encuentra en el ejercicio pero que no afecta en nada las pruebas de la plataforma)
    if int(sucursales) < 1:
        print("Ingrese un numero mayor a 1") #SE TIENE QUE BORRAR
        sucursales = (int(input()))
        continue
    else:
        break

for i in range (0, sucursales): # En este rango le digo que a la lista medicamento le vaya agregando item a item la cantidad de medicamentos por cada sucursal que haya
    while True:# Este es otro condicional que busca que solo se ingresen datos mayores a 1 sino se queda metido en el bucle, solo se exige en el documento del reto3 pero la plataforma no lo evalua
        print (f"Ingresar cantidad del medicamento para la sucursal {i+1}") # SE TIENE QUE BORRAR, Ese {i+1} lo puse asi para que en la pantalla el usuario vea el index desde 1 y no desde 0 como trabaja el bucle
        medicamento.append(int(input())) #Se utiliza el metodo .append para agregar un item al medicamento por cada vuelta que haga el bucle for, osea que por cada sucursal es un item en la variable tipo lista llamada medicamento, de esta forma se sabe que el item 1 de la lista medicamento son los medicamentos de la primera sucursal y asi sucesivamente
        existencias_iniciales.append(int(medicamento[i])) #Aqui le estoy diciendo que lo que se este metiendo en la variable tipo lista llamada medicamento tambien se guarde en esta variable para al final poder calcular el porcentaje
        if int(medicamento[i]) < 1: #Este es el bucle para comprobar si lo que se ingresa en medicamento es mayor a uno, no es necesario que funcion para que la plataforma de la universidad lo apruebe
            print("no ingreso medicamentos, ingrese nuevamente") #SE TIENE QUE BORRAR
            medicamento.pop()
            continue
        else:
            break

print ("Por favor ingrese el numero de la sucursal de cada paciente seguido de su presion sistolica y luego la presion diastolia")#SE TIENE QUE BORRAR
for q in range (0, totalpacientes): #Este for lo utilizo para ingresar la informacion inicial del paciente (sucursal a la que pertence, presion sistonica y presion diatonica) en un mismo renglo, separados por un espacio de acuerdo a como lo exige el reto3
    print (f"Info del paciente {q+1}")#SE TIENE QUE BORRAR
    informacion_inicial_pacientes = str(input()) # Se ingres la info de acuerdo a como lo exige el reto3
    informacion_inicial_pacientes_acumulado = (str(informacion_inicial_pacientes) + " " + str(informacion_inicial_pacientes_acumulado)) #Esta variable tipo lista es donde voy acumulando (concantenando) cada string de caracteres de la variable informacion_inicial_pacientes de forma que se pueda tener a todos los pacientes en una cadena de caracteres para luego convertirla en tipo lista y poder separar y evaluar cada item de la lista

informacion_inicial_pacientes_acumulado = informacion_inicial_pacientes_acumulado.split(" ") #Aca al igual que mas arriba lo que hice es converitr la variable informacinon_inicial_pacientes_acumulado en una lista en donde cada paciente es un bloque de 3 items de la lista, osea que el paciente 1 ocupa los items (0,1,2) de la lista, siendo estos (sucursal a donde pertenece, presion sistonia y presion diastonica), mientras que el paciente 2 ocupa los items (3,4,5) de la lista y asi susesivamente

for n in range (0, len(informacion_inicial_pacientes_acumulado)-1, 3): # Este es el punto central, aqui lo que hago es que la variable tipo lista llamada informacion_inicial_pacientes_acumulados tengo a todos los pacientes en bloques de 3 items de la lista por paciente de forma que se va a evaluar en bloques de 3 items al tiempo a medida que el ciclo da la vuelta, por eso el incremento de 3 en 3 

    sucusral_paciente = int(informacion_inicial_pacientes_acumulado[n])-1 #Aqui se transfiere el item 1 del bloquecito de 3 items que corresponde a la sucursal a la que pertenece el paciente que se encuentra en la variable tipo lista llamada informacion_inicial_pacientes_acumulado, el -1 lo puse por que en el numero de la sucursal ingresado la sucursal 1 seria la sucursal 0 en el ciclo
    presionsis = (int(informacion_inicial_pacientes_acumulado[n+1]))#Aqui se transfiere el item 2 del bloqueito de 3 items que corresponde a la presion sistonica
    presiondiac = (int(informacion_inicial_pacientes_acumulado[n+2]))#Aqui se transfiere el item 3 del bloqueito de 3 items que corresponde a la presion diatonica
    
    #El truco es que cuendo el for da una vuelta con el incremento de 3 items ya para la siguiente iteracion ya va es a transferir los items (3,4,5) de la lista que corresponde a los 3 datos del siguiente paciente y asi susesivamente
    #Inmediatamente se llenan las variables sucursal_paciente, presionsis y presiondiac se evaluan estas variables de acuerdo a la tabla del reto3 y de acuerdo a las condiciones a la variable tipo lista llamada medicamento se le va a restar las dosis en la posicion que corresponda a la sucursal, osea, que si hay 3 sucursales es por que la variable tipo lista llamada medicamento va a tener tres items, uno por cada sucursal
    
    if presionsis < 85 and presiondiac < 65:
        print (f"Categoria del paciente de la sucursal {sucusral_paciente+1} es HIPOTENSION") #SE TIENE QUE BORRAR, solo importa restar el medicamento
        medicamento[sucusral_paciente] -= 10 # Aqui estoy diciendo que cuando se cumpla la condicion se coja de la lista medicamento y se le reste la dosis al item que corresponde a la sucursal que tiene ese inventario de medicamentos
    elif presionsis >= 85 and presionsis < 125 and presiondiac >= 65 and presiondiac < 85:
        print (f"Categoria del paciente de la sucursal {sucusral_paciente+1} es OPTIMA") #SE TIENE QUE BORRAR, solo importa restar el medicamento
    elif presionsis >= 125 and presionsis < 135 and presiondiac >= 85 and presiondiac < 90:
        print (f"Categoria del paciente de la sucursal {sucusral_paciente+1} es NORMAL") #SE TIENE QUE BORRAR, solo importa restar el medicamento
    elif presionsis >= 135 and presionsis < 145 and presiondiac >= 90 and presiondiac < 95:
        print (f"Categoria del paciente de la sucursal {sucusral_paciente+1} es NORMAL ALTA") #SE TIENE QUE BORRAR, solo importa restar el medicamento
        medicamento[sucusral_paciente] -= 5
    elif presionsis >= 145 and presionsis < 165 and presiondiac >= 95 and presiondiac < 105:
        print (f"Categoria del paciente de la sucursal {sucusral_paciente+1} es HIPERTENCION GRADO UNO") #SE TIENE QUE BORRAR, solo importa restar el medicamento
        medicamento[sucusral_paciente] -= 10
    elif presionsis >= 165 and presionsis < 185 and presiondiac >= 105 and presiondiac < 115:
        print (f"Categoria del paciente de la sucursal {sucusral_paciente+1} es HIPERTENCION GRADO DOS") #SE TIENE QUE BORRAR, solo importa restar el medicamento
        medicamento[sucusral_paciente] -= 20
    elif presionsis >= 185 and presiondiac >= 115:
        print (f"Categoria del paciente de la sucursal {sucusral_paciente+1} es HIPERTENCION GRADO TRES") #SE TIENE QUE BORRAR, solo importa restar el medicamento
        medicamento[sucusral_paciente] -= 40
    elif presionsis >= 145 and presiondiac < 95:
        print (f"Categoria del paciente de la sucursal {sucusral_paciente+1} es HIPERTENCION SISTOLICA AISLADA") #SE TIENE QUE BORRAR, solo importa restar el medicamento
        medicamento[sucusral_paciente] -= 30
    
# Una vez que termine de dar vueltas el ciclo ya tenemos la lista de medicamentos con las dosis restadas en cada item que corresponde a cada sucursal

mayor_de_medicamentos = max(medicamento) #Aqui lo que hago que a la variable mayor_de_medicamentos le voy a guardar el maximo valor que se encuentre en los items de la lista llamada medicamento
sucursalmayor = medicamento.index(mayor_de_medicamentos)#Aqui lo que hago es saber en que posicion estaba el numero mas alto ya que esa posicion del item dentro de la lista corresponderia a la sucursal

menor_de_medicamentos = min(medicamento) #Lo mismo de arriba pero buscando el minimo de los dos
sucursalmenor = medicamento.index(menor_de_medicamentos) #Lo mismo de arriba pero buscando la pocicion del minimo para saber a que sucursal corresponde

print (f"La sucursal con menos medicamentos despues de la entrega es la sucursal: {sucursalmenor+1}, con {menor_de_medicamentos}") #SE TIENE QUE BORRAR PERO SE DEBE DE DEJAR EL PRINT DE LAS VARIABLES YA QUE ESTAS SON EXIGIDAS POR EL RETO3, el +1 lo puse por que en los for y todo eso se trabaja desde 0 pero el ejercicio toma la primera sucursal como sucursal 1 mas no curusal 0 como se trabaja dentro del programa
print (f"La sucursal con mayor medicamentos despues de la entrega es la sucursal: {sucursalmayor+1}, con {mayor_de_medicamentos}") #SE TIENE QUE BORRAR PERO SE DEBE DE DEJAR EL PRINT DE LAS VARIABLES YA QUE ESTAS SON EXIGIDAS POR EL RETO3, el +1 lo puse por que en los for y todo eso se trabaja desde 0 pero el ejercicio toma la primera sucursal como sucursal 1 mas no curusal 0 como se trabaja dentro del programa

print("RESUMEN SUCURSALES")#SE TIENE QUE BORRAR

#PARA LOS QUE NO ENTIENDAN QUE PORCENTAJE ES QUE ESTA PIDIENTO EL EJERCICIO
#El porcentaje que esta pidiendo el ejercicio es el porcentaje de medicamentos que se ha gastado en cada sucursal, osea que si en la primera sucursal se ingresaron 100 dosis y al final en esa sucursal quedaron 80 dosis quiere decir que en esa sucursal se han gastado 20 dosis o un 20% del total de dosis solo de esa sucursal

for t in range (0, sucursales): # Con este rango lo que hago es calcular el porcentaje de cada item (sucursal) que se encuentra en la variable tipo lista llamada medicamento, de esta forma si nos exigieron por ejemplo 3 sucursales es por que la variable medicamento tiene 3 items y asi susecivamente
    proporcion_porcentual = float((existencias_iniciales[t] - medicamento[t])*100/existencias_iniciales[t]) #Aqui calculo el porcentaje de dosis que se han gastado, notese que estoy utilizando la lista existencias_iniciales que cree en un principio y que contiene las dosis ingresadas originalmente
    conversion_a_dos_decimales = "{:.2f}".format(proporcion_porcentual) #Aqui lo que hago es darle formato a cada uno de los items que se vayan guardando en la variable proporcion_porcentual para que queden con dos decimales no mas, esto lo busque en GOOGLE
    print (f"La sucursal {t+1}, posee una proporcion porcentual de existencias de {conversion_a_dos_decimales}%")#SE TIENE QUE BORRAR PERO SE DEJA EL PRINT DE {t+1} YA QUE ES UNO DE LOS DATOS QUE EXIGE EL EJERCICIO AL IGUAL QUE LA VARIALBE {conversion_a_dos_decimales} CON EL SIMBOLO % INCLUIDO EN EL PRINT PARA QUE LO VALGA LA PLATAFORMA