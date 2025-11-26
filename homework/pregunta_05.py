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

    resul=[]
    letras=[]
    unica_letra=[]
    numeros=[]
    with open('files/input/data.csv', "r") as archivo:
        for linea in archivo:
            columnas=linea.split()
            letras.append(columnas[0])
            numeros.append(columnas[1])
            if columnas[0] not in unica_letra:
                unica_letra.append(columnas[0])
            else:
                pass
    unica_letra.sort(reverse=False)
    for letra in unica_letra:
        numeros_letra=[]
        for i in range (len(letras)):
            if letras[i]==letra:
                numeros_letra.append(int(numeros[i]))
            else:
                pass
        resul.append((letra,max(numeros_letra),min(numeros_letra)))
        
    return resul


if __name__=="__main__":
    print(pregunta_05())