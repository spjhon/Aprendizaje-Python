# Retro 4

medicamento = list()
sucursal_de_atencion_por_paciente = list()
tipo_medicamento_solicitado_por_paciente = list()
existencias_solicitadas_del_medicamento_por_paciente = list()
presionsis_por_paciente = list()
presiondiac_por_paciente = list()
existencias_programadas_por_medicamento = list()
medicamentos_solicitados_por_sucursal = list()
total_pacientes_por_sucursal = list()
z = float()
promedio = float()
medicamentos_solicitados_por_sucursal_dividido = list()
lista_final = list()

# Aqui se divide el string ingresado y se almacena en cada variable por separado y se convierten a integer
# print("Por favor ingrese el numero de sucursales seguido de cuantos tipos de medicamentos hay y el numero de pacientes totales:")
informacion_inicial = input()
informacion_inicial = informacion_inicial.split(" ")

sucursales = int(informacion_inicial[0])
totaltipomedicamentos = int(informacion_inicial[1])
totalpacientes = int(informacion_inicial[2])

# Aqui se evaluan si los datos ingresados son menores a 1
while True:
    if int(sucursales) < 1:
        sucursales = (int(input()))
        continue
    else:
        break

while True:
    if int(totaltipomedicamentos) < 1:
        totalmedicamentos = (int(input()))
        continue
    else:
        break

# Aqui se divide el string ingresado y se almacena en cada variable por separado y se convierten a integer
for i in range (0, sucursales):
    # print (f"Ingresar la cantidad de cada tipo de medicamento mencionado anteriormente para la sucursal {i+1}")
    informacion_inicial_medicamentos = input()
    informacion_inicial_medicamentos = informacion_inicial_medicamentos.split(" ")
    informacion_inicial_medicamentos2 = informacion_inicial_medicamentos.copy()
    for k in range (0, totaltipomedicamentos):
        informacion_inicial_medicamentos2[k] = int(informacion_inicial_medicamentos2[k])
    existencias_programadas_por_medicamento.append(informacion_inicial_medicamentos2)
    for k in range (0, totaltipomedicamentos):
        informacion_inicial_medicamentos[k] = int(informacion_inicial_medicamentos[k])
    medicamento.append(informacion_inicial_medicamentos)
    
# print (type(informacion_inicial_medicamentos[0]))
 
# print (medicamento)
# print (existencias_programadas_por_medicamento)
for e in range (0, sucursales):
    medicamentos_solicitados_por_sucursal.append(0)

# print (medicamentos_solicitados_por_sucursal)

for s in range (0, sucursales):
    total_pacientes_por_sucursal.append(0)

# print (totalpacientes)
# Aqui se divide el string ingresado y se almacena en cada variable por separado y se convierten a integer
for w in range (0, totalpacientes):
    informacion_inicial_paciente = input()
    informacion_inicial_paciente = informacion_inicial_paciente.split(" ")
    for k in range (0, 5):
        informacion_inicial_paciente[k] = int(informacion_inicial_paciente[k])
    
    x = 0
    sucursal_de_atencion_por_paciente.append((informacion_inicial_paciente[x])-1)
    tipo_medicamento_solicitado_por_paciente.append((informacion_inicial_paciente[x+1])-1)
    existencias_solicitadas_del_medicamento_por_paciente.append(informacion_inicial_paciente[x+2])
    presionsis_por_paciente.append(informacion_inicial_paciente[x+3])
    presiondiac_por_paciente.append(informacion_inicial_paciente[x+4])
    medicamentos_solicitados_por_sucursal[((informacion_inicial_paciente[x])-1)] += existencias_solicitadas_del_medicamento_por_paciente[w]
    total_pacientes_por_sucursal[((informacion_inicial_paciente[x])-1)] += 1
    
# print (sucursal_de_atencion_por_paciente)
# print (tipo_medicamento_solicitado_por_paciente)
# print (existencias_solicitadas_del_medicamento_por_paciente)
# print (presionsis_por_paciente)
# print (presiondiac_por_paciente)
# print (informacion_inicial_paciente)
# Aqui se van a programar las existencias

for a in range (0, totalpacientes):
    
    if presionsis_por_paciente[a] < 85 and presiondiac_por_paciente[a] < 65:
        medicamento[sucursal_de_atencion_por_paciente[a]][tipo_medicamento_solicitado_por_paciente[a]] -= existencias_solicitadas_del_medicamento_por_paciente[a]
        
    elif presionsis_por_paciente[a] >= 85 and presionsis_por_paciente[a] < 125 and presiondiac_por_paciente[a] >= 65 and presiondiac_por_paciente[a] < 85:
        medicamento[sucursal_de_atencion_por_paciente[a]][tipo_medicamento_solicitado_por_paciente[a]] -= 0
        medicamentos_solicitados_por_sucursal[sucursal_de_atencion_por_paciente[a]] -= existencias_solicitadas_del_medicamento_por_paciente[a]
        
    elif presionsis_por_paciente[a] >= 125 and presionsis_por_paciente[a] < 135 and presiondiac_por_paciente[a] >= 85 and presiondiac_por_paciente[a] < 90:
        medicamento[sucursal_de_atencion_por_paciente[a]][tipo_medicamento_solicitado_por_paciente[a]] -= 0
        medicamentos_solicitados_por_sucursal[sucursal_de_atencion_por_paciente[a]] -= existencias_solicitadas_del_medicamento_por_paciente[a]
        
    elif presionsis_por_paciente[a] >= 135 and presionsis_por_paciente[a] < 145 and presiondiac_por_paciente[a] >= 90 and presiondiac_por_paciente[a] < 95:
        medicamento[sucursal_de_atencion_por_paciente[a]][tipo_medicamento_solicitado_por_paciente[a]] -= existencias_solicitadas_del_medicamento_por_paciente[a]
        
    elif presionsis_por_paciente[a] >= 145 and presionsis_por_paciente[a] < 165 and presiondiac_por_paciente[a] >= 95 and presiondiac_por_paciente[a] < 105:
        medicamento[sucursal_de_atencion_por_paciente[a]][tipo_medicamento_solicitado_por_paciente[a]] -= existencias_solicitadas_del_medicamento_por_paciente[a]
        
    elif presionsis_por_paciente[a] >= 165 and presionsis_por_paciente[a] < 185 and presiondiac_por_paciente[a] >= 105 and presiondiac_por_paciente[a] < 115:
        medicamento[sucursal_de_atencion_por_paciente[a]][tipo_medicamento_solicitado_por_paciente[a]] -= existencias_solicitadas_del_medicamento_por_paciente[a]
        
    elif presionsis_por_paciente[a] >= 185 and presiondiac_por_paciente[a] >= 115:
        medicamento[sucursal_de_atencion_por_paciente[a]][tipo_medicamento_solicitado_por_paciente[a]] -= existencias_solicitadas_del_medicamento_por_paciente[a]
        
    elif presionsis_por_paciente[a] >= 145 and presiondiac_por_paciente[a] < 95:
        medicamento[sucursal_de_atencion_por_paciente[a]][tipo_medicamento_solicitado_por_paciente[a]] -= existencias_solicitadas_del_medicamento_por_paciente[a]
    else:
        medicamentos_solicitados_por_sucursal[sucursal_de_atencion_por_paciente[a]] -= existencias_solicitadas_del_medicamento_por_paciente[a]

# print (existencias_solicitadas_del_medicamento_por_paciente)
# print (medicamento)
# print (existencias_programadas_por_medicamento)

for q in range (0, sucursales):
    for a in range (0, totaltipomedicamentos):
        existencias_programadas_por_medicamento[q][a] -= medicamento[q][a]

# print (existencias_programadas_por_medicamento)
# print (medicamentos_solicitados_por_sucursal)
# print (total_pacientes_por_sucursal)
        
# Aqui se imprime lo que se exige en el ejercicio de acuerdo a lo almacenado en las diferentes listas utilizadas
for k in range (0, sucursales):
    x = k
    if totaltipomedicamentos != 0:
        z = float((sum(existencias_programadas_por_medicamento[k]))/totaltipomedicamentos)
    else:
        z = 0
    conversion_a_dos_decimales_de_z = "{:.2f}".format(z)
    if total_pacientes_por_sucursal[k] != 0:
        promedio = ((medicamentos_solicitados_por_sucursal[k])/total_pacientes_por_sucursal[k])
    else:
        promedio = 0
    conversion_a_dos_decimales = "{:.2f}".format(promedio)
    print (x+1)
    index = medicamento[k].index((min(medicamento[k])))
    print (index + 1, min(medicamento[k]))
    index2 = medicamento[k].index((max(medicamento[k])))
    print (index2 + 1, max(medicamento[k]))
    conversion_a_dos_decimales2 = "{:.2f}".format(min(existencias_programadas_por_medicamento[k]))
    conversion_a_dos_decimales3 = "{:.2f}".format(max(existencias_programadas_por_medicamento[k]))
    print (conversion_a_dos_decimales2, conversion_a_dos_decimales_de_z, conversion_a_dos_decimales3)
    print (conversion_a_dos_decimales)

# print (existencias_programadas_por_medicamento)

for m in range (0, sucursales): # Muy interesante forma de copiar una lista
        lista_final.append(existencias_programadas_por_medicamento[m][0])
        

print ((lista_final.index(min(lista_final))+1), min(lista_final))
print ((lista_final.index(max(lista_final))+1), max(lista_final))
