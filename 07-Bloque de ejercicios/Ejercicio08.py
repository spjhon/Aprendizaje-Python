# Ejercicio 8. Crear un programa que permita sacar cuanto es el
# porcentaje de algun numero
# Cuanto es el x% de un numero
#por ejemplo del 20% de 100

numero = int(input("Intruduce el numero: "))
porcentaje = int(input(f"que porcentaje quieres sacar del {numero}: "))
#Para sacar el procentaje de un numero se multiplica por su respectivo decimal
#osea que para sacarle el 20% a 100 hay multiplicar 100*0.20.

operacion = (numero * (porcentaje/100))

print (f"El {porcentaje} de {numero} es: {operacion}")