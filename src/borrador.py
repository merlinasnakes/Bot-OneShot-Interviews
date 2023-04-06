#Version Array de Arrays:

#preguntas = [[1, false, "Una comida que te recuerde a tu hogar"], [2, false, "Elegirías otra época para vivir?"], [3, false, "Cuál es el mejor lugar que conociste"], [4, false, "Hay algo que te haga feliz y sea gratis?",] [5, false, "Cuál fue el último regalo que recibiste?"], [6, false, "Cuál fue el último regalo que hiciste?"], [7, false, "Un viaje pendiente?"], [8, false, "Una canción que te alegre"], [9, false, "Una cosa que te guste pero te sale mal?"], [10, false, "Algo ridículo por lo que te gustaría que te paguen?"], [11, false, "Te gusta bañarte?"], [12, false, "Te gusta comer?"], [13, false, "Te gusta cocinar?",] [14, false, "Cuál es tu comida preferida?"], [15, false, "Tenés mañas? Cuáles?"], [16, false, "Volver al pasado o ir al futuro?"], [17, false, "Qué película viste más veces"], [18, false, "Tenés alguna obsesión, cuál?"]]

# preguntas = ['1,false,Una comida que te recuerde a tu hogar', '2,false,Elegirías otra época para vivir?', '3,false,Cuál es el mejor lugar que conociste', '6,false,Cuál fue el último regalo que hiciste?', '7,false,Un viaje pendiente?', '8,false,Una canción que te alegre', '9,false,Una cosa que te guste pero te sale mal?', '10,false,Algo ridículo por lo que te gustaría que te paguen?', '11,false,Te gusta bañarte?', '12,false,Te gusta comer?', '15,false,Tenés mañas? Cuáles?', '16,false,Volver al pasado o ir al futuro?', '17,false,Qué película viste más veces', '18,false,Tenés alguna obsesión, cuál?']

#Version Diccionario:

#preguntas = {1: "Si fueras animal, ¿qué animal crees que serías?", 2: "¿Cuál es la palabra que más te gusta en este momento?", 3: "¿Cuál es la palabra que menos te gusta?", 4: "Si pudieras ser una mujer/hombre del ambiente artístico. ¿Cuál serías?", 5: "¿Qué te da placer?", 6: "¿Existe algún sonido que te produce placer al escucharlo?", 7: "Si fueras un objeto cuál serías", 8: "Qué es lo que más te gusta del barrio dónde vivís", 9: "Te gustaría hacer una actividad extrema?", 10: "Qué personaje de película o serie te gustaría hacer y por qué", 11: "En qué te gustaría haber sido bueno", 12: "Sí pudieses crear un feriado por qué motivo sería? Se te ocurre cómo se llamaría?", 13: "Si fueses de otro género que sería lo primero que harías", 14: "Tenés un miedo absurdo a algo", 15: "Tuviste alguna experiencia paranormal", 16: "Crees en el amor a primera vista?", 17: "Si fueses embajador qué lugar elegirías para irte a vivir?", 18: "Cuál es tu lugar preferido en tu casa porque", 19: "En qué momento del día tenés tus mejores ideas", 20: "Una comida que te recuerde a tu hogar", 21: "Elegirías otra época para vivir?", 22: "Cuál es el mejor lugar que conociste", 23: "Hay algo que te haga feliz y sea gratis?", 24: "Cuál fue el último regalo que recibiste?", 25: "Cuál fue el último regalo que hiciste?", 26: "Un viaje pendiente?", 27: "Una canción que te alegre", 28: "Una cosa que te guste pero te sale mal?", 29: "Algo ridículo por lo que te gustaría que te paguen?", 30: "Te gusta bañarte?", 31: "Te gusta comer?", 32: "Te gusta cocinar?", 33: "Cuál es tu comida preferida?", 34: "Tenés mañas? Cuáles?", 35: "Volver al pasado o ir al futuro?", 36: "Qué película viste más veces", 37: "Tenés alguna obsesión, cuál?", 38: "Un libro que te gusta en este momento?", 39: "Tenés un sueño recurrente?", 40: "Un juego que te gusta en este momento", 41: "Qué es lo primero que miras en una persona?", 42: "Te irías a vivir al exterior solo?", 43: "Tenés un talento inútil?", 44: "Qué canción elegirías para cantar en un karaoke?", 45: "Una situación vergonzosa de la que haya sido protagonista?", 46: "Alguna cosa que te da vergüenza ajena?", 47: "Tenés algún pensamiento recurrente?", 48: "Si pudieras crear tu lugar en el mundo cómo sería?", 49: "Sos idealista o realista?", 50: "Alguna vez escuchaste alguna conversación sin permiso?", 51: "Cuál fue la primera impresión de la persona que escribió el último comentario en este channel?", 52: "Qué fue lo último que aprendiste?", 53: "A quién te gustaría abrazar?", 54: "Te gustaría hacerle una pregunta a una de las personas presentes?", 55: "Destaca una virtud de una de las personas presentes", 56: "Sentís que te enganchas rápido?", 57: "Te gustan los domingos?", 58: "Sos competitivo?", 59: "Te gustan los chismes?"}

preguntas = [
{   "fue_usada": False,
    "id": 1,
    "pregunta": "Si fueras animal, ¿qué animal crees que serías?"
},
{   "fue_usada": False,
    "id": 2,
    "pregunta": "¿Existe algún sonido que te produce placer al escucharlo?"
},
{   "fue_usada": False,
    "id": 3,
    "pregunta": "Qué es lo que más te gusta del barrio dónde vivís"
},
{   "fue_usada": False,
    "id": 4,
    "pregunta": "Una canción que te alegre el corazón?"
},
{   "fue_usada": False,
    "id": 5,
    "pregunta": "Te gustan los domingos?"
},
{   "fue_usada": False,
    "id": 6,
    "pregunta": "Sos competitivo?"
},
{   "fue_usada": False,
    "id": 7,
    "pregunta": "Sos idealista o realista?"
}
]


#numero_de_pregunta_elegida = preguntas.random.randrange(0, len(preguntas))

#pregunta_requerida = preguntas[6]["fue_usada"]


#def getPregunta():
#    if pregunta_requerida == False:
#        print(preguntas[6]["pregunta"])
#        pregunta_requerida = True



#    diccionario_de_pregunta["estado"] = pregunta[1] == "true"
#    diccionario_de_pregunta["id"] = int(pregunta[0])
#    diccionario_de_pregunta["pregunta"] = pregunta[2]

""" diccionario_de_pregunta = {   
    "estado": False,
    "id": 1,
    "pregunta": " "
    } """



array_de_diccionario = [
    {   
    "estado": False,
    "id": 1,
    "pregunta": "Una comida que te recuerde a tu hogar"
    }
]

array_de_preguntas = []


dict_de_pregunta = {}

def getData():
    preguntas = ['1,true,Una comida que te recuerde a tu hogar?', '2,true,Elegirías otra época para vivir?', '3,true,Cuál es el mejor lugar que conociste', '6,true,Cuál fue el último regalo que hiciste?', '7,true,Un viaje pendiente?', '8,false,Una canción que te alegre?', '9,false,Una cosa que te guste pero te sale mal?', '10,false,Algo ridículo por lo que te gustaría que te paguen?', '11,false,Te gusta bañarte?', '12,false,Te gusta comer?', '15,false,Tenés mañas? Cuáles?', '16,false,Volver al pasado o ir al futuro?', '17,false,Qué película viste más veces', '18,false,Tenés alguna obsesión, cuál?']

    for pregunta in preguntas:
        #array_de_preguntas.append(pregunta.split(','))
        #pregunta = ['1', 'false', 'Una comida que te recuerde a tu hogar']
        pregunta_dividida = pregunta.split(',')
        diccionario_de_pregunta = {
            "estado": pregunta_dividida[1] == "true",
            "id": int(pregunta_dividida[0]),
            "pregunta": pregunta_dividida[2]
        }
        #print(diccionario_de_pregunta)
        array_de_preguntas.append(diccionario_de_pregunta)


getData()    
#print(array_de_preguntas[1]["estado"])

""" for pregunta in array_de_preguntas:
        estadoActual = pregunta["pregunta"]
        print(estadoActual) """
#acá importar la data del módulo preguntas.csv
def pickPregunta(array):
    for pregunta in array:
        estadoActual = pregunta["estado"]
        if estadoActual == "false":
            print(pregunta["pregunta"]) 
            break
        
pickPregunta(array_de_preguntas)        