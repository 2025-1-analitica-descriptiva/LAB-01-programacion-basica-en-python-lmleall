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
import csv

with open('./files/input/data.csv', 'r') as archivo_csv:
        lector_csv = csv.reader(archivo_csv, delimiter="\t")
        
        dic = {}

        for fila in lector_csv:
            #print(fila)
            listacol5 = fila[4].split(",")
            #print(listacol5)
            suma = 0    
            for l in listacol5:
                listallavevalor = l.split(":")
                suma = suma + int(listallavevalor[1])
            #print(suma)
            if fila[0] not in dic:
                dic[fila[0]] = suma
            else:
                dic[fila[0]] = dic[fila[0]] + suma
                
        dic = dict(sorted(dic.items()))
