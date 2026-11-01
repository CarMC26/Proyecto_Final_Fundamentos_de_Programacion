def menu_opciones(opcion):
    #Funciona como barra de opciones
    print("Menú General")
    print("")
    menu = [
        '1. Ubicación', 
        '2. Uso de aplicaciones',
        "3. Profesores",
        "4. Becas",
        "5. Intercambios",
        "6. Semana Tec",
        "7. Asesoramiento",
        "8. Otros",
        "9. Ninguna"
    ]
    for op in menu:
        print(op)
    print("")
    opcion = int(input("Selecciona el número que corresponda a la sección de tu pregunta: "))
    print("")
    return opcion

def preguntas(opcion):
    #Sirve para guardar todas las preguntas en una sola matriz 

    preguntas = [
        [
            "¿No encuentras tu salón?",
            "¿No sabes dónde está un edificio?",
            "¿No sabes cómo llegar a algún lugar?",
            "¿No sabes dónde está algo dentro del campus?",
            "Otros",
            "Regresar a menú general"
        ],
        [
            "¿Tienes dudas sobre mi Tec?",
            "¿Tienes dudas sobre Canvas?",
            "¿Tienes dudas sobre Outlook?",
            "¿Tienes dudas sobre Tec trasporte?",
            "¿Tienes dudas sobre mi Tec celular?",
            "Otros",
            "Regresar a menú general"
        ],
        [
            "¿No sabes donde puedes ver la información para contactar a tu profesor?",
            "¿No sabes que profesor te toco?",
            "¿No sabes cómo hablar con tu profesor?",
            "Otros",
            "Regresar a menú general"
        ],
        [
            "¿Qué tipos de beca existen?",
            "¿Cuáles son los requisitos para obtener una?",
            "¿Cómo y cuándo se solicita la beca?",
            "¿No sabes qué documentos debes entregar?",
            "¿No sabes cómo funciona la asignacion de área/proyecto de Servicio Becario?",
            "¿No sabes si puedes cambiar de horario o de área?",
            "Otros",
            "Regresar a menú general"
        ],
        [
            "¿No sabes qué programas internacionales existen y cuál te conviene?",
            "¿No sabes cuáles son los requisitos para participar (promedio, créditos, idioma)?",
            "¿No sabes cómo y cuándo postularte (convocatorias y fechas límite)?",
            "¿No sabes qué documentos suelen pedir para tu solicitud?",
            "¿No sabes cómo se revalidan materias o se acreditan los créditos?",
            "¿No sabes si puedes usar tu beca y/o financiamiento durante el programa?",
            "Otros",
            "Regresar a menú general"
        ],
        [
            "¿No sabes qué es Semana Tec?",
            "¿No sabes cuándo te toca Semana Tec?",
            "¿No sabes qué pasa si el cupo se llena?",
            "¿No sabes si puedes cambiarte de Semana Tec?",
            "¿No sabes cómo se evalúa?",
            "¿No sabes qué pasa si faltas o no entregas un trabajo?",
            "Otros",
            "Regresar a menú general"
        ],
        [
            "¿No sabes con quién asesorarte sobre tu carrera?",
            "¿No sabes dónde ver las asesorías de profesores?",
            "¿No sabes a qué asesorías externas puedes acudir?",
            "¿No sabes dónde buscar oportunidades?",
            "¿No sabes qué hacer si necesitas orientación?",
            "Otros",
            "Regresar a menú general"
        ]
    ]
    
    return preguntas[opcion - 1]


def guardar_en_historial(historial, categoria, seleccion):
    #Crea una matriz donde guarda todas las preguntas ya hechas
    matriz = preguntas()
    if 1 <= categoria <= len(matriz) and 1 <= seleccion <= len(matriz[categoria - 1]):
        historial.append(matriz[categoria - 1][seleccion - 1])

def buscar_preguntas(texto, preguntas):
    #Funciona como un buscador que busca palabras clave dentro de la matriz de preguntas
    palabras = texto.lower().split()
    resultados = []

    for menu in preguntas:
        for pregunta in menu:
            pregunta_minuscula = pregunta.lower()

            if any(palabra in pregunta_minuscula for palabra in palabras):
                resultados.append(pregunta)

    return resultados

def main():
    historial = []
    opcion = 0
    opcion = menu_opciones(opcion)
    while opcion < 9 and opcion >= 1:
        #Funciona como un almacenador de infromacion ademas de que permite preguntar mas de una ves 
        match opcion:
            case 1:
                #Funciona para resolver cada caso particularmente 
                print("Menú de ubicación")
                preguntas(opcion)
                opcion_ubicacion = int(input("Selecciona el número que corresponda a la sección de tu pregunta: "))

                guardar_en_historial(historial, opcion, opcion_ubicacion)
                if opcion_ubicacion <= 6:
                    #Funciona para no recibir valores erroneos
                    match opcion_ubicacion:
                        #Funciona para resolver cada caso de esta seccion particularmente 
                        case 1:
                            print("")
                        case 2:
                            print("")
                        case 3:
                            print("")
                        case 4:
                            print("")
                        case 5:
                            print("")
                        case 6:
                            menu_opciones(opcion)
                else:
                    #funciona para dar una segunda oportunidad en caso de error 
                    print()
                    print("Seleccione una de las opciones")
                    print()
                    preguntas(opcion)
                    opcion_ubicacion = int(input("Selecciona el número que corresponda a la sección de tu pregunta: "))
               
                       
                       

                    guardar_en_historial(historial, opcion, opcion_ubicacion)
            case 2:
                print("Menú de aplicaciones")
                preguntas(opcion)
                opcion_applicacion = int(input("Selecciona el número que corresponda a la sección de tu pregunta: "))

                guardar_en_historial(historial, opcion, opcion_applicacion)
                if opcion_applicacion <= 7:
                    match opcion_applicacion:
                        case 1:
                            print()
                        case 2:
                            print()
                        case 3:
                            print()
                        case 4:
                            print()
                        case 5:
                            print()
                        case 6:
                            print()
                        case 7:
                            menu_opciones(opcion)
                       
                else:
                    print()
                    print("Seleccione una de las opciones")
                    print()
                    print("Menú de aplicaciones")
                    preguntas(opcion)
                    opcion_applicacion = int(input("Selecciona el número que corresponda a la sección de tu pregunta: "))
                    

                    guardar_en_historial(historial, opcion, opcion_applicacion)
            case 3:
                print("Menú de profesores")
                preguntas(opcion)
                opcion_profesores = int(input("Selecciona el número que corresponda a la sección de tu pregunta: "))

                guardar_en_historial(historial, opcion, opcion_profesores)
                if opcion_profesores <= 5:
                    match opcion_profesores:
                        case 1:
                            print("")
                        case 2:
                            print("")
                        case 3:
                            print("")
                        case 4:
                            print("")
                        case 5:
                            menu_opciones(opcion)
                        
                else:
                    print()
                    print("Seleccione una de las opciones")
                    print()
                    print("Menú de profesores")
                    preguntas(opcion)
                    opcion_profesores = int(input("Selecciona el número que corresponda a la sección de tu pregunta: "))


                    guardar_en_historial(historial, opcion, opcion_profesores)
            case 4:
                print("Menú de becas")
                preguntas(opcion)
                opcion_becas = int(input("Selecciona el número que corresponda a la sección de tu pregunta: "))

                guardar_en_historial(historial, opcion, opcion_becas)
                if opcion_becas <= 8:
                    match opcion_becas:
                        case 1:
                            print("")
                        case 2:
                            print("")
                        case 3:
                            print("")
                        case 4:
                            print("")
                        case 5:
                            print("")
                        case 6:
                            print()
                        case 7:
                            print()
                        case 8:
                            menu_opciones(opcion)
                        
                else:
                    print(" ")
                    print("Seleccione una de las opciones")
                    print()
                    print("Menú de becas")
                    preguntas(opcion)
                    opcion_becas = int(input("Selecciona el número que corresponda a la sección de tu pregunta: "))

                
                

                    guardar_en_historial(historial, opcion, opcion_becas)
            case 5:
                print("Menú de intercambios")
                preguntas(opcion)
                opcion_Interacional = int(input("Selecciona el número que corresponda a la sección de tu pregunta: "))

                guardar_en_historial(historial, opcion, opcion_Interacional)
                if opcion_Interacional <= 8:
                    match opcion_Interacional:
                        case 1:
                            print("")
                        case 2:
                            print("")
                        case 3:
                            print("")
                        case 4:
                            print("")
                        case 5:
                            print("")
                        case 6:
                            print()
                        case 7:
                            print()
                        case 8:
                            menu_opciones(opcion)
                        
                else:
                    print()
                    print("Seleccione una de las opciones")
                    print()
                    print("Menú de intercambios")
                    preguntas(opcion)
                    opcion_Interacional = int(input("Selecciona el número que corresponda a la sección de tu pregunta: "))
                

                    guardar_en_historial(historial, opcion, opcion_Interacional)
            case 6:
                print("Menú Semana Tec")
                preguntas(opcion)
                opcion_Semana_Tec = int(input("Selecciona el número que corresponda a la sección de tu pregunta: "))

                guardar_en_historial(historial, opcion, opcion_Semana_Tec)
                if opcion_Semana_Tec <= 8:
                    match opcion_Semana_Tec:
                        case 1:
                            print("")
                        case 2:
                            print("")
                        case 3:
                            print("")
                        case 4:
                            print("")
                        case 5:
                            print("")
                        case 6:
                            print()
                        case 7:
                            print()
                        case 8:
                            menu_opciones(opcion)
                        
                else:
                    print()
                    print("Seleccione una de las opciones")
                    print()
                    print("Menú Semana Tec")
                    preguntas(opcion)
                    opcion_Semana_Tec = int(input("Selecciona el número que corresponda a la sección de tu pregunta: "))

                    


                    guardar_en_historial(historial, opcion, opcion_Semana_Tec)
            case 7:
                print("Menú Asesoramiento")
                preguntas(opcion)
                opcion_Asesoramiento = int(input("Selecciona el número que corresponda a la sección de tu pregunta: "))

                guardar_en_historial(historial, opcion, opcion_Asesoramiento)
                if opcion_Asesoramiento <= 7:
                    match opcion_Asesoramiento:
                        case 1:
                            print("")
                        case 2:
                            print("")
                        case 3:
                            print("")
                        case 4:
                            print("")
                        case 5:
                            print()
                        case 6:
                            print()
                        case 7:
                            menu_opciones(opcion)
                        
                else:
                    print()
                    print("Seleccione una de las opciones")
                    print()
                    print("Menú Asesoramiento")
                    preguntas(opcion)
                    opcion_Asesoramiento = int(input("Selecciona el número que corresponda a la sección de tu pregunta: "))


                    guardar_en_historial(historial, opcion, opcion_Asesoramiento)
            case 8:
                busqueda = input("¿Qué estás buscando? ")
                historial.append("Búsqueda: " + busqueda)

                resultados = buscar_preguntas(busqueda, preguntas())

                if resultados:
                    print("Encontré estas preguntas relacionadas:")
                    for pregunta in resultados:
                        print(pregunta)
                else:
                    print("No encontré preguntas relacionadas.")

                
                
                
    print()
    #Funciona como historial para guardar preguntas 
    if historial:
        print("Historial de preguntas:")
        for pregunta_hecha in historial:
            print(pregunta_hecha)
    print("Espero haber resuelto tu duda")

                
        
        
main()










