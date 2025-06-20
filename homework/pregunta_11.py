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
import csv

with open('./files/input/data.csv', 'r') as archivo_csv:
        lector_csv = csv.reader(archivo_csv, delimiter="\t")
        
        dic = {}

        for fila in lector_csv:
            #print(fila)
            listacol4 = fila[3].split(",")
            #print(listacol4)           
            for letra in listacol4:
                if letra not in dic:
                    dic[letra] = int(fila[1])
                else:
                    dic[letra] = dic[letra] + int(fila[1])
        dic = dict(sorted(dic.items()))
