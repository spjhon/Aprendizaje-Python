# Ejercicio 10.
# Ingresar la nota de 15 alumnos y sacar por pantalla cuantos han aprobado y cuantos han perdido
perdido = int()
gano = int()
alumnos = int(input("Cuantos alumnos va a ingresar al sistema?: "))
i = int(1)
nota = str()
notaeva = float()
for i in range (1, alumnos+1):
    nota = (input(f"Ingrese la nota el estudiante numero {i}: "))
    try:
        float(nota)
    except ValueError:
        print ("No se puede por que hay una o mas letras")
        exit()
    notaeva = float(nota)
    if notaeva < 3:
        perdido += 1
    else:
        gano += 1

print (f"Los alumos que aprobaron la materia fueron {gano}, mientras que los alumnos que perdieron la materia fueron {perdido}")