# Reto 02, Entrega de medicamentos
dosis = int()
ayuno = str()
glucosa = float()
tipomedicamento1 = int(0)
tipomedicamento2 = int(0)
neutro = int(0)
pacientes = int(0)
existencias1 = int(input())
existencias2 = int(input())
while existencias1 > 0 and existencias2 > 0:
    
    ayuno = input()
    
    glucosa = input()
    if ayuno != "si" and ayuno != "sI" and ayuno != "Si" and ayuno != "SI" and ayuno != "no" and ayuno != "NO" and ayuno != "No" and ayuno != "nO":
        
        neutro += 1
        pacientes += 1
    else:
        glucosatrans = float(glucosa)
        if ayuno != "no" and ayuno != "NO" and ayuno != "No" and ayuno != "nO":
            if glucosatrans < 0.07:
                existencias2 -= 4
                tipomedicamento2 += 1
                pacientes += 1
                
            elif glucosatrans >= 0.07 and glucosatrans < 0.1:
                neutro += 1
                pacientes += 1
                
            elif glucosatrans >= 0.1 and glucosatrans < 0.125:
                existencias1 -= 4
                tipomedicamento1 += 1
                pacientes += 1
                
            elif glucosatrans >= 0.125:
                existencias1 -= 7
                tipomedicamento1 += 1
                pacientes += 1
                
        else:
            if glucosatrans < 0.14:
                neutro += 1
                pacientes += 1

            elif glucosatrans >= 0.14 and glucosatrans < 0.2:
                existencias1 -= 5
                tipomedicamento1 += 1
                pacientes += 1
                
            elif glucosatrans >= 0.2:
                existencias1 -= 9
                tipomedicamento1 += 1
                pacientes += 1
                
else:
    print (pacientes)
    porcentaje = float((tipomedicamento1*100)/pacientes)
    format_float = "{:.2f}".format(porcentaje)
    print (f"{tipomedicamento1} {format_float}%")
    porcentaje = float((tipomedicamento2*100)/pacientes)
    format_float2 = "{:.2f}".format(porcentaje)
    print (f"{tipomedicamento2} {format_float2}%")