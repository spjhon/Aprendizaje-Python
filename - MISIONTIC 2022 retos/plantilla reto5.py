# Plantilla para desarrollar Reto 5
#
def leerArchivo():
    with open(********, 'r') as datafile:
        linea= datafile.*****()
        encabezado= *****.rstrip('\n').split(',')

        # Iniciar una matriz nula para la informacion de los pacientes
        matriz= []
        #
        # Inicia un vector con un espacio en blanco para guardar la concatenacion de Ciudad y Departamento por ej.: Leticia Amazonas
        sucursales= [' ']*32
        #
        linea = *****.readline()
        while linea:
            fila = linea.rstrip('\n').split(',')

            # Concatena city_name y department_name en indice id_branch-1, ten en cuenta el inicie de cada atributo
            sucursales[int(fila[5])-1]= fila[*****]+ " " + *****[4]
            #
            # Adiciona una fila a la matriz de pacientes
            matriz.********(fila)
            #
            # Lee la siguiente linea del archivo CSV
            ***** = datafile.readline()

    return matriz, sucursales, encabezado
#
def main():
    # Arreglos de datos que se obtienen de la funcion
    pacientes, centrales, columnas= leerArchivo()

    # Obtiene los indices de las columnas utilizadas en el proceso
    ***** = columnas.index('gender')
    i_branch = columnas.index('*****')
    i_ps = columnas.index('systolic_pressure')
    i_pd = columnas.index('*****')
    ***** = columnas.index('medicine_quantity')
    hombres = 0
    mujeres = *****
    len_pacientes = len(*****)
    cant_med = *****

    # Capturar la central ingresada como Entrada
    input_central= int(input())
    #
    for i in range(*****):
        if int(pacientes[i][i_branch])== *****:
            entrega= False
            sis, dia = int(pacientes[*****][i_ps]), int(pacientes[*****][i_pd])
            if sis < 91 and dia < 63:
                entrega= *****
            elif 162 <= sis < 188 and 105 <= dia < 119:
                entrega= True
            elif 188 <= sis < 201 and ***** <= dia < *****:
                entrega= *****
            elif ***** <= sis < ***** and 126 <= dia < 146:
                entrega= True
            elif sis >= 214 and dia >= *****:
                entrega= *****
            elif sis >= 152 and dia < 77:
                entrega= *****
            else:
                entrega= *****

            if entrega:
                if pacientes[i][i_gender]==*****:
                    hombres += 1
                else :
                    mujeres += *****

                # Acumula Cantidad Total de Medicamentos solicitados por el Cliente
                cant_med += int(*****)

    # Salidas esperadas
    print(f"{input_central} {centrales[input_central-1]}")
    print("scheduled patients")
    print(f'male {******}')
    print(***************)
    print(f'total {******}')
    print('scheduled medicine quantity')
    print('mean {:.2f}'.format(*****/(*****)))
    print(*************************)

if __name__=='__main__':
    *******