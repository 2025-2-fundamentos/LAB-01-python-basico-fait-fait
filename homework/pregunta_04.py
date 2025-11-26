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
    resul=[]
    meses=[]
    unico_mes=[]
    with open('files/input/data.csv', "r") as archivo:
        for linea in archivo:
            columnas=linea.split()
            fechas=columnas[2]
            _, mes, _ = fechas.split('-')
            meses.append(mes)
            if mes not in unico_mes:
                unico_mes.append(mes)
            else:
                pass
    
    unico_mes.sort()
    for mes in unico_mes:
        n_veces=meses.count(mes)
        resul.append((mes,n_veces))

    return resul

if __name__=="__main__":
    print(pregunta_04())