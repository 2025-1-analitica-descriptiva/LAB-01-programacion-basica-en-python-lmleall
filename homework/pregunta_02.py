"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """

import csv
with open(r"C:\Github\Descriptiva\Laboratorios\LAB-01-programacion-basica-en-python-lmleall\files\input\data.csv", 'r') as archivo_csv:
    
    lector_csv = csv.reader(archivo_csv)
    
    lista = []
    for fila in lector_csv:
        columna_1 = fila[0]
        letra = columna_1[0]
        lista.append(letra)

    dic = {}
    for letra in lista:
        if letra not in dic:
            dic[letra] = 1
        else: 
            dic[letra] = dic[letra] + 1
    
    # Convertir el diccionario a una lista de tuplas y ordenarla alfabéticamente
      
    lista_tuplas = sorted(list(dic.items()))

    # Imprimir la lista de tuplas   
    
    print(lista_tuplas)

