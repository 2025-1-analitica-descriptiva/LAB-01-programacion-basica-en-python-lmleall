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

    with open('./files/input/data.csv', 'r') as archivo_csv:
            dic_letras = {}
        
            for fila in archivo_csv:
                columnas = fila.strip().split('\t')
                letra = columnas[0]
                valor = int(columnas[1])
                
                if letra not in dic_letras:                    
                    dic_letras[letra] = [valor]
                else:
                    dic_letras[letra].append(valor)
                
            lista_tuplas =[]
            for letra in sorted(dic_letras.keys()):
                maximo = max(dic_letras[letra])
                minimo = min(dic_letras[letra])
                lista_tuplas.append((letra, maximo, minimo))

            return lista_tuplas   
            
    


