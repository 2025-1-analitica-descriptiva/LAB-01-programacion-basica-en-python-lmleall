"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

   """

import csv
with open('./files/input/data.csv', 'r') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        dic = {}
    
        for fila in lector_csv:
            a = fila[0]
            col = a.split("\t")
            letra = col[0]
            num = col[1]
            if letra not in dic:
                listaxletra = []
                listaxletra.append(int(num))
                dic[letra] = listaxletra
            else:
                dic[letra] = dic[letra] + [int(num)]
            
        for letra in dic:
            maximo = max(dic[letra])
            minimo = min(dic[letra])
            dic[letra] = (maximo,minimo)


        listatuplas = sorted(list(dic.items()))
        
        listatrituplas = []
        for tupla in listatuplas:
             tuplaanid = tupla[1]
             tuplamod = (tupla[0],tuplaanid[0],tuplaanid[1])
             listatrituplas.append(tuplamod)
                 
        print(listatrituplas)

            
    


