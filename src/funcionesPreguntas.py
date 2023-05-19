import csv
 

def getData(filename):
    array_de_diccionario=[]
    with open(filename, encoding="utf-8") as dataPreguntas:
        for linea in dataPreguntas.readlines():
            linea_dividida = linea.replace("\n", "").split(';')
            diccionario_de_linea = {
                "id": int(linea_dividida[0]),
                "estado": linea_dividida[1] == "True",
                "pregunta": linea_dividida[2]
            }
            array_de_diccionario.append(diccionario_de_linea)
    return array_de_diccionario

#print(getData("preguntas"))  

        
def pickPregunta():
    array= getData("preguntas")
    for index, diccionario_de_pregunta in enumerate(array):
        estadoActual = diccionario_de_pregunta["estado"]
        if estadoActual == False:
            preguntaElegida = diccionario_de_pregunta["pregunta"]
            array[index]["estado"] = True
            writeData("preguntas", array)
            return(preguntaElegida) 



def writeData(filename, array):
    with open(filename, 'w', encoding="utf-8") as dataPreguntas:
        for line in array:
            registro = str(line["id"]) + ";" + str(line["estado"]) + ";" + line["pregunta"] + "\n"    
            dataPreguntas.write(registro)   
        
             
        



