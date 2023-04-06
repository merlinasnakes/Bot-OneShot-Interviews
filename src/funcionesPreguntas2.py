import csv 

with open('preguntas.txt') as dataPreguntas:
  print(dataPreguntas.readline())
  
array_de_preguntas = []
array_de_linea = []
linea= dataPreguntas.readline()

def getLinea():
    for linea in dataPreguntas:
        array_de_linea.append(linea)
        
getLinea()
print(array_de_linea)        
  
""" def getData():
    for pregunta in dataPreguntas:
        pregunta_dividida = pregunta.split(';')
        diccionario_de_pregunta = {
            "estado": pregunta_dividida[1] == "true",
            "id": int(pregunta_dividida[0]),
            "pregunta": pregunta_dividida[2]
        }
        #print(diccionario_de_pregunta)
        array_de_preguntas.append(diccionario_de_pregunta)
getData()  """     