# Reto 01, deteccion de diabetes
print ("Buenas tardes /Si desayuno escriba si /Si esta en ayuno escriba no")
ayuno = input()
print ("Por favor introduzca el nivel de glucosa en g/dl")
glucosa = float(input())

if ayuno != "si" and ayuno != "sI" and ayuno != "Si" and ayuno != "SI" and ayuno != "no" and ayuno != "NO" and ayuno != "No" and ayuno != "nO":
    print ("error en los datos")
else:
    print ("Su categoria de riesgo de diabetes es: ")
    if ayuno != "no" and ayuno != "NO" and ayuno != "No" and ayuno != "nO":
        if glucosa < 0.07:
            print ("HIPOGLUSEMIA")
        elif glucosa >= 0.07 and glucosa < 0.1:
            print ("Normal")
        elif glucosa >= 0.1 and glucosa < 0.125:
            print ("Elevado")
        elif glucosa >= 0.125:
            print ("Diabetes")
        else:
            print ("Valor incorrecto")
    else:
        if glucosa < 0.14:
            print ("Normal")
        elif glucosa >= 0.14 and glucosa < 0.2:
            print ("Elevado")
        elif glucosa >= 0.2:
            print ("Diabetes")
        else:
            print ("Valor incorrecto")

