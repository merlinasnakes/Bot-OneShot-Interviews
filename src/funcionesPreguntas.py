import csv
 

def getData(filename):
    array_de_diccionario=[]
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
  

        
def pickPregunta():
    array= getData("preguntas.csv")
    for diccionario_de_pregunta in array:
        estadoActual = diccionario_de_pregunta["estado"]
        if estadoActual == False:
            preguntaElegida = diccionario_de_pregunta["pregunta"]
            writeData("preguntas.csv")
            return(preguntaElegida) 

def writeData(filename):
    with open(filename, 'w', encoding="utf-8") as dataPreguntas:
        dataPreguntas.write(diccionario_de_pregunta["estado"] == True)            
        
print(pickPregunta())



