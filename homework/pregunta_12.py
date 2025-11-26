"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    diccionario = {}
    numeros = []
    with open("files/input/data.csv", "r") as archivo:
        for fila in archivo:
            columna = fila.split()
            valores = columna[4].split(",")
            if columna[0] not in diccionario:
                diccionario[columna[0]] = 0
            for valor in valores:
                _, numero = valor.split(":")
                numeros.append(int(numero))
                diccionario[columna[0]] += int(numero)

    diccionario = dict(sorted(diccionario.items()))
    return diccionario


if __name__ == "__main__":
    print(pregunta_12())