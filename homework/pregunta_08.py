"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """
import csv
with open('./files/input/data.csv', 'r') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)

        dic = {}
        
        for fila in lector_csv:
            #print(fila)
            listafila = []
            a = fila[0]
            col = a.split("\t")
            #print(col)
            if int(col[1]) not in dic:
                listaxnum = []
                listaxnum.append(col[0])
                dic[int(col[1])] = listaxnum
            else:
                dic[int(col[1])] = dic[int(col[1])] + [col[0]]

        #Convertir cada lista asociada a una llave en un conjunto (set) que por definición no permite duplicados y posteriormente volver a convertir en lista. Finalmente organizar alfabeticamente. 
        for key in dic:
             dic[key] = sorted(list(set(dic[key])))

        dic = sorted(dic.items())
print(dic)