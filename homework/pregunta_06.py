"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
import csv
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
                 listatotal.append(l)   
        
        dic = {}
        for lista in listatotal:
            if lista[0] not in dic: 
                listaxllave = []   
                listaxllave.append(int(lista[1]))
                dic[lista[0]] = listaxllave
            else:
                dic[lista[0]] = dic[lista[0]] + [int(lista[1])]

        for llave in dic:
            maximo = max(dic[llave])
            minimo = min(dic[llave])
            dic[llave] = (minimo,maximo)

        #print(listatotal)
        #print(dic)

        listatuplas = sorted(list(dic.items()))
        
        listatrituplas = []
        for tupla in listatuplas:
             tuplaanid = tupla[1]
             tuplamod = (tupla[0],tuplaanid[0],tuplaanid[1])
             listatrituplas.append(tuplamod)

        print(listatrituplas)