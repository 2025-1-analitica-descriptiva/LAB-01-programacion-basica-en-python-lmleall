"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
import csv
with open('./files/input/data.csv', 'r') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        
        listameses = []
        for fila in lector_csv:
            columna_1 = fila[0]
            columna_3 = columna_1.split("\t")
            fecha = columna_3[2]
            mes = fecha.split("-")[1]
            listameses.append(mes)

        from collections import Counter
        listatuplas = sorted(Counter(listameses).items())

   
