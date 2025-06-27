"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    with open('./files/input/data.csv', 'r') as archivo_csv:
        lista_tuplas = []

        for fila in archivo_csv:
            columnas = fila.strip().split('\t')

            letra = columnas[0]
            elementos_col4 = columnas[3].split(',')  # Columna 4: lista separada por coma
            elementos_col5 = columnas[4].split(',')  # Columna 5: lista separada por coma

            tupla = (letra, len(elementos_col4), len(elementos_col5))
            lista_tuplas.append(tupla)

    return lista_tuplas

