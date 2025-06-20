"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
import csv
import collections

with open('./files/input/data.csv', 'r') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)

        listatotal = []
        
        for fila in lector_csv:
            #print(fila)
            listafila = []
            for col in fila:
                 if ":" in col:
                    listaprov = col.split(":")
                    listafila.append(listaprov)
            posicion = listafila[0][0].index("\t")
            listafila[0][0] = listafila[0][0][posicion+1:]
            #print(listafila)

            for l in listafila:
                 listatotal.append(l[0])
            
        #print(listatotal)
        #Se crea un objeto tipo Counter que es diferente a un objeto tipo dic
        count = collections.Counter(listatotal)
        #print(dic)
        #Posteriormente se convierte este objeto en una lista de tuplas (.items()) y se organiza alfabeticamente con sorted. Para finalmente construir un diccionario a partir de estas tuplas con dict() 
        dic = dict(sorted(count.items()))
