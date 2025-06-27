"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
def pregunta_11():
    with open('./files/input/data.csv', 'r') as archivo_csv:
        dic = {}

        for fila in archivo_csv:
            columnas = fila.strip().split('\t')
            valor_col2 = int(columnas[1])        # Columna 2 (número)
            letras_col4 = columnas[3].split(',') # Columna 4 (letras separadas por coma)

            for letra in letras_col4:
                if letra not in dic:
                    dic[letra] = valor_col2
                else:
                    dic[letra] += valor_col2

        return dict(sorted(dic.items()))
