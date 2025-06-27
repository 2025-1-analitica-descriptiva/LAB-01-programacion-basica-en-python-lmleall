"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """



    with open('./files/input/data.csv', 'r') as archivo_csv:
        dic = {}

        for fila in archivo_csv:
            columnas = fila.strip().split('\t')
            letra = columnas[0]              # Columna 1
            valores_col5 = columnas[4].split(',')  # Columna 5, con pares clave:valor

            suma = 0
            for par in valores_col5:
                clave, valor = par.split(':')
                suma += int(valor)

            if letra not in dic:
                dic[letra] = suma
            else:
                dic[letra] += suma

        return dict(sorted(dic.items()))
