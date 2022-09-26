# Reto 02, Entrega de medicamentos
dosis = int()
ayuno = list()
glucosa = list()
tipomedicamento1 = int(0)
tipomedicamento2 = int(0)
neutro = int(0)

print ("#####  Preguntas de Inventario  #####")
print ("\n")
print ("Favor ingresar existencias del medicamento 1 :")
existencias1 = int(input())
print ("Favor ingresar existencias medicamento 2: ")
existencias2 = int(input())
print ("Favor ingresar cantidad de pacientes a atender: ")
pacientes = int(input())
print ("\n")
print ("\n")
print ("##### Preguntas para el paciente #####")
print ("\n")
for i in range(0, pacientes):
    print (f"Ingrese datos del paciente {i}")
    print (f"El paciente {i} se encuentra en ayunas?, introduzca 'si' o 'no'")
    ayuno.append (input())
    print ("Por favor introduzca el nivel de glucosa en g/dl")
    glucosa.append (input())
print ("\n")
print ("\n")
print ("##### Su categoria de riesgo de diabetes es: #####")
print ("\n")
for z in range(0, pacientes):
    print ("\n")
    if existencias1 > 0 and existencias2 > 0:
        if ayuno[z] != "si" and ayuno[z] != "sI" and ayuno[z] != "Si" and ayuno[z] != "SI" and ayuno[z] != "no" and ayuno[z] != "NO" and ayuno[z] != "No" and ayuno[z] != "nO":
            print (f"Al paciente {z} no se le entrego medicamento ya que no dijo si estaba en ayuno o no")
            neutro += 1
        else:
            glucosatrans = float(glucosa[z])
            if ayuno[z] != "no" and ayuno[z] != "NO" and ayuno[z] != "No" and ayuno[z] != "nO":
                if glucosatrans < 0.07:
                    existencias2 -= 4
                    tipomedicamento2 += 1
                    print (f"el paciente {z} HIPOGLUSEMIA")
                elif glucosatrans >= 0.07 and glucosatrans < 0.1:
                    neutro += 1
                    print (f"el paciente {z} Normal")
                elif glucosatrans >= 0.1 and glucosatrans < 0.125:
                    existencias1 -= 4
                    tipomedicamento1 += 1
                    print (f"el paciente {z} Elevado")
                elif glucosatrans >= 0.125:
                    existencias1 -= 7
                    tipomedicamento1 += 1
                    print (f"el paciente {z} Diabetes")
                else:
                    print ("Valor incorrecto")
            else:
                if glucosatrans < 0.14:
                    neutro += 1
                    print (f"el paciente {z} Normal")
                elif glucosatrans >= 0.14 and glucosatrans < 0.2:
                    existencias1 -= 5
                    tipomedicamento1 += 1
                    print (f"el paciente {z} Elevado")
                elif glucosatrans >= 0.2:
                    existencias1 -= 9
                    tipomedicamento1 += 1
                    print (f"el paciente {z} Diabetes")
                else:
                    print ("Valor incorrecto")
    else:
        print ("\n")
        print ("Se acabaron los medicamentos")

print ("\n")
print ("\n") 
print ("CANTIDAD DE PACIENTES ATENDIDOS")
print (pacientes)
print ("\n")
print ("CANTIDAD DE PACIENTES QUE SE LES DIO MEDICAMENTO 1")
print (tipomedicamento1)
print ("PORCENTAJE DE PACIENTES CON MEDICAMENTO 1 RESPECTO AL TOTAL ATENDIDO")
porcentaje = float((tipomedicamento1*100)/pacientes)
format_float = "{:.2f}".format(porcentaje)
print(format_float+"%")
print ("\n")
print ("CANTIDAD DE PACIENTES QUE SE LES DIO MEDICAMENTO 2")
print(tipomedicamento2)
print ("PORCENTAJE DE PACIENTES CON MEDICAMENTO 2 RESPECTO AL TOTAL ATENDIDO")
porcentaje = float((tipomedicamento2*100)/pacientes)
format_float2 = "{:.2f}".format(porcentaje)
print(format_float2+"%")
print ("\n")
print ("CANTIDAD DE PACIENTES QUE NO RECIBIERON MEDICAMENTO ALGUNO")
print (neutro)
print ("PORCENTAJE DE PACIENTES QUE NO SE LES SUMINISTRO MEDICAMENTO CON RESPECTO AL TOTAL ATENDIDO")
porcentaje = float((neutro*100)/pacientes)
format_float3 = "{:.2f}".format(porcentaje)
print(format_float3+"%")
print ("\n")