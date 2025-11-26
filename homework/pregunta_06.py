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
    diccionario={}
    result=[]
    with open('files/input/data.csv', "r") as archivo:
        for linea in archivo:
            columnas=linea.split()
            pares=columnas[4].split(",")
            for par in pares:
                letra,numero=par.split(':')
                numero=int(numero)
                if letra not in diccionario:
                    diccionario[letra]=[]
                diccionario[letra].append(numero)
    diccionario=dict(sorted(diccionario.items()))

    for letra, valor in diccionario.items():
        result.append((letra,min(valor), max(valor)))

    return result

if __name__=="__main__":
    print(pregunta_06())

        