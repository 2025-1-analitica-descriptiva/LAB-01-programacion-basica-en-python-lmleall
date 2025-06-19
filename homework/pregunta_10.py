"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
import csv

with open('./files/input/data.csv', 'r') as archivo_csv:
        lector_csv = csv.reader(archivo_csv, delimiter="\t")
        
        listatrituplas = []

        for fila in lector_csv:
            #print(fila)
            listacol4 = fila[3].split(",")
            listacol5 = fila[4].split(",")
            #print(listacol4)
            #print(listacol5)
            tritupla = (fila[0],len(listacol4),len(listacol5))
            listatrituplas.append(tritupla)

print(listatrituplas)