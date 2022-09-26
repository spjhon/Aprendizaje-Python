#Reto 03, Inventario sucursales

sucursales = int()
totalpacientes = int()
medicamento = list()
existencias_iniciales = list()
informacion_inicial = str()
informacion_inicial_pacientes = str()
informacion_inicial_pacientes_acumulado = str()

informacion_inicial = input()
informacion_inicial = informacion_inicial.split(" ")

for o in range (0, 1):
    sucursales = int(informacion_inicial[o])
    totalpacientes = int(informacion_inicial[o+1])
    break

while True:
    if int(sucursales) < 1:
        sucursales = (int(input()))
        continue
    else:
        break

for i in range (0, sucursales):
    while True:
        medicamento.append(int(input()))
        existencias_iniciales.append(int(medicamento[i]))
        if int(medicamento[i]) < 1:
            medicamento.pop()
            continue
        else:
            break

for q in range (0, totalpacientes):
    informacion_inicial_pacientes = str(input())
    informacion_inicial_pacientes_acumulado = (str(informacion_inicial_pacientes) + " " + str(informacion_inicial_pacientes_acumulado))

informacion_inicial_pacientes_acumulado = informacion_inicial_pacientes_acumulado.split(" ")

for n in range (0, len(informacion_inicial_pacientes_acumulado)-1, 3):

    sucusral_paciente = int(informacion_inicial_pacientes_acumulado[n])-1
    presionsis = (int(informacion_inicial_pacientes_acumulado[n+1]))
    presiondiac = (int(informacion_inicial_pacientes_acumulado[n+2]))
    
    if presionsis < 85 and presiondiac < 65:
        medicamento[sucusral_paciente] -= 10
    elif presionsis >= 85 and presionsis < 125 and presiondiac >= 65 and presiondiac < 85:
        medicamento[sucusral_paciente] -= 0
    elif presionsis >= 125 and presionsis < 135 and presiondiac >= 85 and presiondiac < 90:
        medicamento[sucusral_paciente] -= 0
    elif presionsis >= 135 and presionsis < 145 and presiondiac >= 90 and presiondiac < 95:
        medicamento[sucusral_paciente] -= 5
    elif presionsis >= 145 and presionsis < 165 and presiondiac >= 95 and presiondiac < 105:
        medicamento[sucusral_paciente] -= 10
    elif presionsis >= 165 and presionsis < 185 and presiondiac >= 105 and presiondiac < 115:
        medicamento[sucusral_paciente] -= 20
    elif presionsis >= 185 and presiondiac >= 115:
        medicamento[sucusral_paciente] -= 40
    elif presionsis >= 145 and presiondiac < 95:
        medicamento[sucusral_paciente] -= 30
    
mayor_de_medicamentos = max(medicamento)
sucursalmayor = medicamento.index(mayor_de_medicamentos)

menor_de_medicamentos = min(medicamento)
sucursalmenor = medicamento.index(menor_de_medicamentos)

print (f"{sucursalmenor+1} {menor_de_medicamentos}")
print (f"{sucursalmayor+1} {mayor_de_medicamentos}") 

for t in range (0, sucursales):
    proporcion_porcentual = float((existencias_iniciales[t] - medicamento[t])*100/existencias_iniciales[t])
    conversion_a_dos_decimales = "{:.2f}".format(proporcion_porcentual)
    print (f"{t+1} {conversion_a_dos_decimales}%")
 