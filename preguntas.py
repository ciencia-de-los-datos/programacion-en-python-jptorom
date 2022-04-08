"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    import csv
    with open("data.csv",newline='') as t:
        datos = csv.reader(t,delimiter ="\t")
        columns =list(datos)
    
    suma = 0
    for row in columns:
        suma += int(row[1])

    return suma



def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    import csv
    with open("data.csv",newline='') as t:
        datos = csv.reader(t,delimiter ="\t")
        columns =list(datos)
    listica = [row[0] for row in columns]
    frecuencia = {}
    for n in listica:
        if n in frecuencia:
            frecuencia[n] += 1
        else: 
            frecuencia[n] =1
    '''Se ordena el diccionario en orden alfabetico'''
    xy = dict(sorted(frecuencia.items(), key=lambda item: item[0]))
    '''Se convierte el diccionario en tuplas'''
    l1 = list(xy.items())
    
    return l1



def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    import csv
    from collections import Counter
    with open("data.csv",newline='') as t:
        datos = csv.reader(t,delimiter ="\t")
        columns =list(datos)
    listica = list()
    for i in columns:
        a= i[:2]
        listica.append(a)
    sumatoria= {}
    for row in listica:
        key = row[0]
        value = int(row[1])
        if key in sumatoria:
            sumatoria[key] += value
        else:
            sumatoria[key] = value
    '''Se ordena el diccionario en orden alfabetico'''
    xy = dict(sorted(sumatoria.items(), key=lambda item: item[0]))
    '''Se convierte el diccionario en tuplas'''
    l1 = list(xy.items())


    
    return l1


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    import csv
    from collections import Counter
    with open("data.csv",newline='') as t:
        datos = csv.reader(t,delimiter ="\t")
        columns =list(datos)
    listica = list()
    for i in columns:
        a= i[2]
        listica.append(a)
    listota = list()
    for m in listica:
        b=m[5:7]
        listota.append(b)
    frecuencia={}
    for n in listota:
        if n in frecuencia:
            frecuencia[n] += 1
        else: 
            frecuencia[n] =1
    '''Se ordena el diccionario en orden alfabetico'''
    xy = dict(sorted(frecuencia.items(), key=lambda item: item[0]))
    '''Se convierte el diccionario en tuplas'''
    l1 = list(xy.items())
    
    return l1

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]
    
    """
    import csv
    from collections import Counter
    from operator import itemgetter
    with open("data.csv",newline='') as t:
        datos = csv.reader(t,delimiter ="\t")
        columns =list(datos)
    l1 = [row[0] for row in columns]
    l2 = [int(fila[1]) for fila in columns]
    l3 = list(zip(l1,l2))
    dicc= {}
    for row in l3:
        clave = row[0]
        valor = []
        val = row[1]
        if clave in dicc:
            dicc[clave].append(val)
        else:
            dicc[clave]=valor
            dicc[clave].append(val)
    dicc = [(clave,max(valor),min(valor)) for clave,valor in dicc.items()]
    dicc = sorted(dicc,key = itemgetter(0), reverse = False)
    
    return dicc

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    import csv
    from operator import itemgetter
    with open ("data.csv","r") as file:
        data = file.readlines()
    datatemp = list()
    data1= [row[:-1] for row in data]
    data2 = [str(row).split("\t")[-1] for row in data1]
    data4 = []
    data5=[]
    for row in data2:
        a= row.split(",")
        data4.extend(a)
    for row in data4:
        b= row.split(":")
        data5.extend(b)
    x= data5[0::2]
    y = data5[1::2]
    xy = zip(x,y)
    dicc= {}
    for row in xy:
        clave = row[0]
        valor = []
        val = int(row[1])
        if clave in dicc:
            dicc[clave].append(val)
        else:
            dicc[clave]=valor
            dicc[clave].append(val)
    dicc = [(clave,min(valor),max(valor)) for clave,valor in dicc.items()]
    dicc = sorted(dicc,key = itemgetter(0), reverse = False)
    
    return dicc


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    import csv
    from collections import Counter
    from operator import itemgetter
    with open("data.csv",newline='') as t:
        datos = csv.reader(t,delimiter ="\t")
        columns =list(datos)
    l1 = [row[0] for row in columns]
    l2 = [int(fila[1]) for fila in columns]
    l3 = list(zip(l1,l2))
    dicc= {}
    for row in l3:
        clave = row[1]
        valor = []
        val = row[0]
        if clave in dicc:
            dicc[clave].append(val)
        else:
            dicc[clave]=valor
            dicc[clave].append(val)
    xy = dict(sorted(dicc.items(), key=lambda item: item[0]))
    '''Se convierte el diccionario en tuplas'''
    l1 = list(xy.items())
    l1
    
    return l1


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    import csv
    from collections import Counter
    from operator import itemgetter
    with open("data.csv",newline='') as t:
        datos = csv.reader(t,delimiter ="\t")
        columns =list(datos)
    l1 = [row[0] for row in columns]
    l2 = [int(fila[1]) for fila in columns]
    l3 = set(list(zip(l1,l2)))
    l5 = sorted(l3, key = lambda ord : ord[0])
    dicc= {}
    for row in l5:
        clave = row[1]
        valor = []
        val = row[0]
        if clave in dicc:
            if val in valor:
                next
            else:
                dicc[clave].append(val)
        else:
            dicc[clave]=valor
            dicc[clave].append(val)
    '''Se ordena el diccionario en orden alfabetico'''
    xy = dict(sorted(dicc.items(), key=lambda item: item[0]))
    '''Se convierte el diccionario en tuplas'''
    l4 = list(xy.items())
    
    return l4


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    with open ("data.csv","r") as file:
        data = file.readlines()
    datatemp = list()
    data1= [row[:-1] for row in data]
    data2 = [str(row).split("\t")[-1] for row in data1]
    data4 = []
    data5=[]
    for row in data2:
        a= row.split(",")
        data4.extend(a)
    for row in data4:
        b= row.split(":")
        data5.extend(b)
    x= data5[0::2]
    y = data5[1::2]
    xy = zip(x,y)
    dicc= {}
    for row in xy:
        clave = row[0]
        valor = []
        val = int(row[1])
        if clave in dicc:
            dicc[clave] += 1
        else:
            dicc[clave] = 1
    xy = dict(sorted(dicc.items(), key=lambda item: item[0]))
    
    return xy


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    '''Se extrae la información del csv'''
    import csv
    from operator import itemgetter
    with open ("data.csv","r") as file:
        data = file.readlines()
    data1= [row for row in data]
    '''Necesito que la columna de Letras se repita por cada registro de la columna 5'''
    data2 = [str(row).split("\t")[-1].split(",") for row in data1]
    '''Necesito que la columna de Letras se repita por cada registro de la columna 4'''
    data3 = [str(row).split("\t")[-2].split(",") for row in data1]

    '''Voy a contar el número de elementos que tiene cada columna 5'''
    data99 = [len(row) for row in data2]
    data98 = [row[0] for row in data]
    '''Voy a contar el número de elementos que tiene cada columna 4'''
    data97 = [len(row) for row in data3]
    data96=zip(data98,data97,data99)
    
    return list(data96)


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    return


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    return
