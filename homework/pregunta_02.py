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
    resul=[]
    letras=[]
    unica_letra=[]
    with open('files/input/data.csv', "r") as archivo:
        for linea in archivo:
            columnas=linea.split()
            letras.append(columnas[0])
            if columnas[0] not in unica_letra:
                unica_letra.append(columnas[0])
            else:
                pass
    unica_letra.sort(reverse=False)
    for letra in unica_letra:
        n_cantidad=letras.count(letra)
        resul.append((letra,n_cantidad))
    return resul

if __name__=="__main__":
    print(pregunta_02())