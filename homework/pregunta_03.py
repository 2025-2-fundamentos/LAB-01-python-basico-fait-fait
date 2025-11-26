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
        sum_num=0
        for i in range (len(letras)):
            if letras[i]==letra:
                sum_num+=int(numeros[i])
            else:
                pass
        resul.append((letra,sum_num))
        
    return resul
if __name__=="__main__":
    print(pregunta_03())