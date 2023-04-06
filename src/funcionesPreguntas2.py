import csv 

with open('preguntas.txt') as dataPreguntas:
  #print(dataPreguntas.readlines())
array_de_linea=[]

def getData():
    for linea in dataPreguntas.readlines():
        linea_dividida = linea.split(';')
        diccionario_de_linea = {
            "estado": linea_dividida[1] == "true",
            "id": int(linea_dividida[0]),
            "linea": linea_dividida[2]
        }
        array_de_lineas.append(diccionario_de_linea)
        
getData()    


""" def getLinea():
    for linea in dataPreguntas.readlines():
        array_de_linea.append(linea)
        
getLinea()
print(array_de_linea)        
   """