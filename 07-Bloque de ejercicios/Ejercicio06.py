
# Mostrar todas las tablas de multiplicar del 1 al 10
# mostrando el titulo de la tabla y luego las multiplicaciones

multiplicador = int(0)
for control in range(0, 11):
    print (f"TABLA DE MULTIPLICAR DEL: {control}")
    for multiplicador in range (0, 10):
        print (f"{control} x {multiplicador} = {control*multiplicador}")


