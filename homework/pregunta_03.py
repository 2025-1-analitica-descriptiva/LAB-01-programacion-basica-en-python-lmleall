"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    
    with open('./files/input/data.csv', 'r') as archivo_csv:
            
            suma_letras = {}
            
            for fila in archivo_csv:
                columnas = fila.strip().split('\t')
                valor = int(columnas[1])
                letra = columnas[0]
                
                if letra not in suma_letras:
                    suma_letras[letra] = valor
                else:
                    suma_letras[letra] += valor

            lista_tuplas = sorted(suma_letras.items())
            return lista_tuplas
 
    

   