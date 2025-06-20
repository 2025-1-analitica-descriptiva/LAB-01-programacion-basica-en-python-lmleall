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

import csv
with open(r"C:\Github\Descriptiva\Laboratorios\LAB-01-programacion-basica-en-python-lmleall\files\input\data.csv", 'r') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    suma = 0
    for fila in lector_csv:        
        columna_1 = fila[0]
        columna_2 = columna_1[2]
        
        suma = suma + int(columna_2)
    