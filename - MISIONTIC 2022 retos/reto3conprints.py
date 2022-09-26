#Reto 03, Inventario sucursales

sucursales = int()
totalpacientes = int()
medicamento = list()
existencias_iniciales = list()
informacion_inicial = str()
informacion_inicial_pacientes = str()
informacion_inicial_pacientes_acumulado = str()

print("Por favor ingrese el numero de sucursales seguido del numero de pacientes totales:")
informacion_inicial = input()
informacion_inicial = informacion_inicial.split(" ")

for o in range (0, 1):
    sucursales = int(informacion_inicial[o])
    totalpacientes = int(informacion_inicial[o+1])
    break

while True:
    if int(sucursales) < 1:
        print("Ingrese un numero mayor a 1")
        sucursales = (int(input()))
        continue
    else:
        break

for i in range (0, sucursales):
    while True:
        print (f"Ingresar cantidad del medicamento para la sucursal {i+1}")
        medicamento.append(int(input()))
        existencias_iniciales.append(int(medicamento[i]))
        if int(medicamento[i]) < 1:
            print("no ingreso medicamentos, ingrese nuevamente")
            medicamento.pop()
            continue
        else:
            break

print ("Por favor ingrese el numero de la sucursal de cada paciente seguido de su presion sistolica y luego la presion diastolia")
for q in range (0, totalpacientes):
    print (f"Info del paciente {q+1}")
    informacion_inicial_pacientes = str(input())
    informacion_inicial_pacientes_acumulado = (str(informacion_inicial_pacientes) + " " + str(informacion_inicial_pacientes_acumulado))

informacion_inicial_pacientes_acumulado = informacion_inicial_pacientes_acumulado.split(" ")

for n in range (0, len(informacion_inicial_pacientes_acumulado)-1, 3):

    sucusral_paciente = int(informacion_inicial_pacientes_acumulado[n])-1
    presionsis = (int(informacion_inicial_pacientes_acumulado[n+1]))
    presiondiac = (int(informacion_inicial_pacientes_acumulado[n+2]))
    
    if presionsis < 85 and presiondiac < 65:
        print (f"Categoria del paciente de la sucursal {sucusral_paciente+1} es HIPOTENSION")
        medicamento[sucusral_paciente] -= 10
    elif presionsis >= 85 and presionsis < 125 and presiondiac >= 65 and presiondiac < 85:
        print (f"Categoria del paciente de la sucursal {sucusral_paciente+1} es OPTIMA")
        medicamento[sucusral_paciente] -= 0
    elif presionsis >= 125 and presionsis < 135 and presiondiac >= 85 and presiondiac < 90:
        print (f"Categoria del paciente de la sucursal {sucusral_paciente+1} es NORMAL")
        medicamento[sucusral_paciente] -= 0
    elif presionsis >= 135 and presionsis < 145 and presiondiac >= 90 and presiondiac < 95:
        print (f"Categoria del paciente de la sucursal {sucusral_paciente+1} es NORMAL ALTA")
        medicamento[sucusral_paciente] -= 5
    elif presionsis >= 145 and presionsis < 165 and presiondiac >= 95 and presiondiac < 105:
        print (f"Categoria del paciente de la sucursal {sucusral_paciente+1} es HIPERTENCION GRADO UNO")
        medicamento[sucusral_paciente] -= 10
    elif presionsis >= 165 and presionsis < 185 and presiondiac >= 105 and presiondiac < 115:
        print (f"Categoria del paciente de la sucursal {sucusral_paciente+1} es HIPERTENCION GRADO DOS")
        medicamento[sucusral_paciente] -= 20
    elif presionsis >= 185 and presiondiac >= 115:
        print (f"Categoria del paciente de la sucursal {sucusral_paciente+1} es HIPERTENCION GRADO TRES")
        medicamento[sucusral_paciente] -= 40
    elif presionsis >= 145 and presiondiac < 95:
        print (f"Categoria del paciente de la sucursal {sucusral_paciente+1} es HIPERTENCION SISTOLICA AISLADA")
        medicamento[sucusral_paciente] -= 30
    
mayor_de_medicamentos = max(medicamento)
sucursalmayor = medicamento.index(mayor_de_medicamentos)

menor_de_medicamentos = min(medicamento)
sucursalmenor = medicamento.index(menor_de_medicamentos)

print (f"La sucursal con menos medicamentos despues de la entrega es la sucursal: {sucursalmenor+1}, con {menor_de_medicamentos}") 
print (f"La sucursal con mayor medicamentos despues de la entrega es la sucursal: {sucursalmayor+1}, con {mayor_de_medicamentos}") 

print("RESUMEN SUCURSALES")

for t in range (0, sucursales): 
    proporcion_porcentual = float((existencias_iniciales[t] - medicamento[t])*100/existencias_iniciales[t]) 
    conversion_a_dos_decimales = "{:.2f}".format(proporcion_porcentual) 
    print (f"La sucursal {t+1}, posee una proporcion porcentual de existencias de {conversion_a_dos_decimales}%")
 