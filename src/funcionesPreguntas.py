import csv
 

def getData(filename):
    array_de_diccionario=[]
    with open(filename, encoding="utf-8") as dataPreguntas:
        for linea in dataPreguntas.readlines():
            linea_dividida = linea.replace("\n", "").split(';')
            diccionario_de_linea = {
                "estado": linea_dividida[1] == "true",
                "id": int(linea_dividida[0]),
                "linea": linea_dividida[2]
            }
            array_de_diccionario.append(diccionario_de_linea)
    return array_de_diccionario
         
#print(getData("preguntas.csv"))

def pickPregunta(array):
    for pregunta in array:
        estadoActual = pregunta["estado"]
        if estadoActual == False:
            print(pregunta["pregunta"]) 
            break
        
pickPregunta(array_de_preguntas)     