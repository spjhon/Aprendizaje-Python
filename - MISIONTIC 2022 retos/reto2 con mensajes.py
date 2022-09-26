# Reto 02, Entrega de medicamentos
dosis = int()
ayuno = str()
glucosa = float()
tipomedicamento1 = int(0)
tipomedicamento2 = int(0)
neutro = int(0)
pacientes = int(0)
print ("Favor ingresar existencias del medicamento 1 :")
existencias1 = int(input())
print ("Favor ingresar existencias medicamento 2: ")
existencias2 = int(input())

while existencias1 > 0 and existencias2 > 0:
    print (f"El paciente se encuentra en ayunas?, introduzca 'si' o 'no'")
    ayuno = input()
    print ("Por favor introduzca el nivel de glucosa en g/dl")
    glucosa = input()
    if ayuno != "si" and ayuno != "sI" and ayuno != "Si" and ayuno != "SI" and ayuno != "no" and ayuno != "NO" and ayuno != "No" and ayuno != "nO":
        print (f"Al paciente no se le entrego medicamento ya que no dijo si estaba en ayuno o no")
        neutro += 1
        pacientes += 1
    else:
        glucosatrans = float(glucosa)
        if ayuno != "no" and ayuno != "NO" and ayuno != "No" and ayuno != "nO":
            if glucosatrans < 0.07:
                existencias2 -= 4
                tipomedicamento2 += 1
                pacientes += 1
                print ("el paciente tiene HIPOGLUSEMIA")
            elif glucosatrans >= 0.07 and glucosatrans < 0.1:
                neutro += 1
                pacientes += 1
                print ("el paciente esta Normal")
            elif glucosatrans >= 0.1 and glucosatrans < 0.125:
                existencias1 -= 4
                tipomedicamento1 += 1
                pacientes += 1
                print ("el paciente esta Elevado")
            elif glucosatrans >= 0.125:
                existencias1 -= 7
                tipomedicamento1 += 1
                pacientes += 1
                print ("el paciente tiene Diabetes")
            else:
                print ("Valor incorrecto")
        else:
            if glucosatrans < 0.14:
                neutro += 1
                pacientes += 1
                print ("el paciente Normal")
            elif glucosatrans >= 0.14 and glucosatrans < 0.2:
                existencias1 -= 5
                tipomedicamento1 += 1
                pacientes += 1
                print ("el paciente Elevado")
            elif glucosatrans >= 0.2:
                existencias1 -= 9
                tipomedicamento1 += 1
                pacientes += 1
                print ("el paciente Diabetes")
            else:
                print ("Valor incorrecto")
else:
    print ("CANTIDAD DE PACIENTES ATENDIDOS")
    print (pacientes)
    print ("CANTIDAD DE PACIENTES QUE SE LES DIO MEDICAMENTO 1 CON SU PORCENTAJE ES: ")
    porcentaje = float((tipomedicamento1*100)/pacientes)
    format_float = "{:.2f}".format(porcentaje)
    print (f"{tipomedicamento1} {format_float}%")
    print ("CANTIDAD DE PACIENTES QUE SE LES DIO MEDICAMENTO 2 CON SU PORCENTAJE ES: ")
    porcentaje = float((tipomedicamento2*100)/pacientes)
    format_float2 = "{:.2f}".format(porcentaje)
    print (f"{tipomedicamento2} {format_float2}%")