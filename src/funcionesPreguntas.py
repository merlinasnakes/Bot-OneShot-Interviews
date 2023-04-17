import csv
 
array_de_diccionario=[]

def getData(filename):
    with open(filename, encoding="utf-8") as dataPreguntas:
        for linea in dataPreguntas.readlines():
            linea_dividida = linea.replace("\n", "").split(';')
            diccionario_de_linea = {
                "id": int(linea_dividida[0]),
                "estado": linea_dividida[1] == "true",
                "pregunta": linea_dividida[2]
            }
            array_de_diccionario.append(diccionario_de_linea)
    return array_de_diccionario

def pickPregunta(array):
    for diccionario_de_pregunta in array:
        estadoActual = diccionario_de_pregunta["estado"]
        if estadoActual == False:
            return(diccionario_de_pregunta["pregunta"]) 
            
        
#print(pickPregunta(getData("preguntas.csv")))
