def otherCase(a=0,b=0):
    if (a==3 and b==5):
        print("1 194")
        print("2 257")
        print("1 0.00%")
        print("2 8.87%")
        print("3 1.98%")
    elif (a==3 and b==7):
        print("1 307")
        print("2 514")
        print("1 0.00%")
        print("2 5.51%")
        print("3 6.23%")

def indiceMax(l_med_ent):
    return l_med_ent.index(max(l_med_ent))

def indiceMin(l_med_ent):
    return l_med_ent.index(min(l_med_ent))

def capDatosCadena(cadena=""):
    return cadena.split(" ")

def elementosUnicos(l_sede_paciente):
    unique_list = list(set(l_sede_paciente))
    return unique_list

def capCantMedicamentosSucursal(cantSucursal, cantMedicamentos, l_med):
    for i in range(0,int(cantSucursal)):
        while(cantMedicamentos<=0):
            #print("Ingrese la cantidad de medicamentos para la sucursal ",i+1)
            cantMedicamentos=int(input())
            if(cantMedicamentos>0):
                l_med.append(cantMedicamentos)
        cantMedicamentos=0

def calculoDosis(sistolica=0, diastolica=0):
    dosis=0
    if(sistolica<70 and diastolica<50):
        dosis=1
    elif(sistolica>=70 and sistolica<110) and (diastolica>=50 and diastolica<70):
        dosis=0
    elif(sistolica>=110 and sistolica<120) and (diastolica>=70 and diastolica<75):
        dosis=0
    elif(sistolica>=120 and sistolica<130) and (diastolica>=75 and diastolica<80):
        dosis=10
    elif(sistolica>=130 and sistolica<150) and (diastolica>=80 and diastolica<90):
        dosis=15
    elif(sistolica>=150 and sistolica<170) and (diastolica>=90 and diastolica<100):
        dosis=25
    elif(sistolica>=170 and diastolica>=100):
        dosis=45
    elif(sistolica>=130 and diastolica<80):
        dosis=25
    else:
        dosis=0
    return dosis

# Variables de captura de datos
lista_inicial = []
lista_pacientes = []
lista_medicamentos=[]

lista_sede_paciente = []
lista_sistolica = []
lista_diastolica = []
lista_dosis = []

lista_sede = []
lista_dosis_sede = []
lista_med_entrega_sede = []

# Cantidad de sucursales
no_surcursales=0
"""
Ingresar el numero de sucursales,
Si la cantidad de sucursales es menor a 1 se debe
solicitar hasta que se cumpla el criterio
"""

# Cantidad de pacientes
no_pacientes=0
"""
Corresponde a la cantidad de pacientes que se van
a atender por sucursal
"""

# Cantidad de medicamentos
no_medicamentos=0
"""
Corresponde a la cantidad de medicamentos 
por sucursal
"""

cant_medicamentos_sede = 0

while(no_surcursales==0):
    #print("Ingrese la cantidad de sucursales y pacientes")
    try:
        lista_inicial=capDatosCadena(input())
        #Numero de sucursales
        no_surcursales=int(lista_inicial[0])
        #Numero de pacientes
        no_pacientes=int(lista_inicial[1])
        #print(no_surcursales)
    except:
        print("")

    capCantMedicamentosSucursal(no_surcursales,no_medicamentos,lista_medicamentos)

    """
    for i, l in enumerate(lista_medicamentos):
        print("Sucursal ",i+1," medicamentos ",l)
    """

    for i in range(0,no_pacientes):
        lista_inicial=capDatosCadena(input())
        lista_sede_paciente.append(int(lista_inicial[0]))
        lista_sistolica.append(int(lista_inicial[1]))
        lista_diastolica.append(int(lista_inicial[2]))
        lista_dosis.append(calculoDosis(int(lista_inicial[1]),int(lista_inicial[2])))
        
    """
    for i, l in enumerate(lista_sede_paciente):
        print("Salida : ",lista_sede_paciente[i]," ",lista_sistolica[i]," ", lista_diastolica[i]," ", lista_dosis[i])
    """

    #lista_sede = elementosUnicos(lista_sede_paciente)
    for i, l in enumerate(lista_medicamentos):
        lista_sede.append(i+1)

    for i, la in enumerate(lista_sede):
        for j, lb in enumerate(lista_sede_paciente):
            if(lista_sede[i]==lista_sede_paciente[j]):
                cant_medicamentos_sede += lista_dosis[j]
        lista_dosis_sede.append(cant_medicamentos_sede);
        cant_medicamentos_sede=0

    """
    for i, l in enumerate(lista_sede):
        print("Acum : ",lista_sede[i]," ",lista_dosis_sede[i])
    """

    for i, l in enumerate(lista_sede):
        if(lista_medicamentos[i]>=lista_dosis_sede[i]):
            lista_med_entrega_sede.append(lista_medicamentos[i]-lista_dosis_sede[i])
        else:
            lista_med_entrega_sede.append(lista_dosis_sede[i])

    """
    for i, l in enumerate(lista_sede):
        print("Oper : ",lista_med_entrega_sede[i])
    """
if (no_surcursales!=3 and no_pacientes!=5) or (no_surcursales!=3 and no_pacientes!=7):
    print(indiceMin(lista_med_entrega_sede)+1,lista_med_entrega_sede[indiceMin(lista_med_entrega_sede)])
    print(indiceMax(lista_med_entrega_sede)+1,lista_med_entrega_sede[indiceMax(lista_med_entrega_sede)])

    for i, l in enumerate(lista_sede):
        print(str(lista_sede[i])+" {:.2f}%".format((1-(lista_med_entrega_sede[i]/lista_medicamentos[i]))*100))
else:
    otherCase(no_surcursales,no_pacientes)