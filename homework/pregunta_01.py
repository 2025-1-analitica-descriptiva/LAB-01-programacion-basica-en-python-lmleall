"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
     
    with open('./files/input/data.csv', 'r') as archivo_csv:
        suma = 0
        for fila in archivo_csv:        
            columnas = fila.strip().split('\t')
            valor = int(columnas[1])
            
            suma += valor

    return suma

        
 