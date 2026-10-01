def menu_opciones(opcion):
    #Funciona como barra de opciones
    print("Menú General")
    print("")
    print("1. Ubicación")
    print("2. Uso de aplicaciones")
    print("3. Profesores")
    print("4. Becas")
    print("5. Intercambios")
    print("6. Semana Tec")
    print("7. Asesoramiento")
    print("8. Ninguna")
    print("")
    opcion = int(input("Selecciona el número que corresponda a la sección de tu pregunta: "))
    print("")
    return opcion

def menu_ubicacion():
    #Son las diferentes opciones de respuesta respecto a este tema
    print("Menu de ubicacion")
    print("")
    print("1. ¿No encuentras tu salón?")
    print("2. ¿No sabes dónde está un edificio?")
    print("3. ¿No sabes cómo llegar a algún lugar?")
    print("4. ¿No sabes dónde está algo dentro del campus?")
    print("5. Otros")
    print("6. Regresar a menú general")
    print("")
    return

def menu_aplicaciones():
    print("Menú aplicaciones")
    print()
    print("1. ¿Tienes dudas sobre mi Tec?")
    print("2. ¿Tienes dudas sobre Canvas?")
    print("3. ¿Tienes dudas sobre Outlook?")
    print("4. ¿Tienes dudas sobre Tec trasporte?")
    print("5. ¿Tienes dudas sobre mi Tec celular?")
    print("6. Otros")
    print("7. Regresar a menú general")
    print()
    return

def menu_profesores():
    print("Menú profesores")
    print()
    print("1. ¿No sabes donde puedes ver la información para contactar a tu profesor?")
    print("2. ¿No sabes que profesor te toco?")
    print("3. ¿No sabes cómo hablar con tu profesor?")
    print("4. Otros")
    print("5. Regresar a menú general")
    print()
    return
    
def menu_becas():
    print("Menú becas")
    print()
    print("1. ¿Qué tipos de beca existen?")
    print("2. ¿Cuáles son los requisitos para obtener una?")
    print("3. ¿Cómo y cuándo se solicita la beca?")
    print("4. ¿No sabes qué documentos debes entregar?")
    print("5. ¿No sabes cómo funciona la asignacion de área/proyecto de Servicio Becario?")
    print("6. ¿No sabes si puedes cambiar de horario o de área?")
    print("7. Otros")
    print("8. Regresar a menú general")
    print()
    return

def menu_semana_tec():
    print("Menú Semana Tec")
    print()
    print("1. ¿No sabes qué es Semana Tec?")
    print("2. ¿No sabes cuándo te toca Semana Tec?")
    print("3. ¿No sabes qué pasa si el cupo se llena?")
    print("4. ¿No sabes si puedes cambiarte de Semana Tec?")
    print("5. ¿No sabes cómo se evalúa?")
    print("6. ¿No sabes qué pasa si faltas o no entregas un trabajo?")
    print("7. Otros")
    print("8. Regresar a menú general")
    print()
    return

def menu_interacional():
    print("Menú Programas Internacionales")
    print()
    print("1. ¿No sabes qué programas internacionales existen y cuál te conviene?")
    print("2. ¿No sabes cuáles son los requisitos para participar (promedio, créditos, idioma)?")
    print("3. ¿No sabes cómo y cuándo postularte (convocatorias y fechas límite)?")
    print("4. ¿No sabes qué documentos suelen pedir para tu solicitud?")
    print("5. ¿No sabes cómo se revalidan materias o se acreditan los créditos?")
    print("6. ¿No sabes si puedes usar tu beca y/o financiamiento durante el programa?")
    print("7. Otros")
    print("8. Regresar a menú general")
    print()
    return


def menu_asesoramiento():
    print("Menú Asesoramiento")
    print()
    print("1. ¿No sabes con quién asesorarte sobre tu carrera?")
    print("2. ¿No sabes dónde ver las asesorías de profesores?")
    print("3. ¿No sabes a qué asesorías externas puedes acudir?")
    print("4. ¿No sabes dónde buscar oportunidades?")
    print("5. ¿No sabes qué hacer si necesitas orientación?")
    print("6. Otros")
    print("7. Regresar a menú general")
    print()
    return


def main():
    opcion = 0
    opcion = menu_opciones(opcion)
    while opcion < 8:
        #Funciona como un almacenador de infromacion ademas de que permite preguntar mas de una ves 
        match opcion:
            case 1:
                #Funciona para resolver cada caso particularmente 
                menu_ubicacion()
                opcion_ubicacion = int(input("Selecciona el número que corresponda a la sección de tu pregunta: "))
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
                    menu_ubicacion()
                    opcion_ubicacion = int(input("Selecciona el número que corresponda a la sección de tu pregunta: "))
               
                       
                       
            case 2:
                menu_aplicaciones()
                opcion_applicacion = int(input("Selecciona el número que corresponda a la sección de tu pregunta: "))
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
                    menu_aplicaciones()
                    opcion_applicacion = int(input("Selecciona el número que corresponda a la sección de tu pregunta: "))
                    
            case 3:
                menu_profesores()
                opcion_profesores = int(input("Selecciona el número que corresponda a la sección de tu pregunta: "))
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
                    menu_profesores()
                    opcion_profesores = int(input("Selecciona el número que corresponda a la sección de tu pregunta: "))

            case 4:
                menu_becas()
                opcion_becas = int(input("Selecciona el número que corresponda a la sección de tu pregunta: "))
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
                    menu_becas()
                    opcion_becas = int(input("Selecciona el número que corresponda a la sección de tu pregunta: "))

                
                
            case 5:
                menu_interacional()
                opcion_Interacional = int(input("Selecciona el número que corresponda a la sección de tu pregunta: "))
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
                    menu_interacional()
                    opcion_Interacional = int(input("Selecciona el número que corresponda a la sección de tu pregunta: "))
                
            case 6:
                menu_semana_tec()
                opcion_Semana_Tec = int(input("Selecciona el número que corresponda a la sección de tu pregunta: "))
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
                    menu_semana_tec()
                    opcion_Semana_Tec = int(input("Selecciona el número que corresponda a la sección de tu pregunta: "))

                    

            case 7:
                menu_asesoramiento()
                opcion_Asesoramiento = int(input("Selecciona el número que corresponda a la sección de tu pregunta: "))
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
                    menu_asesoramiento()
                    opcion_Asesoramiento = int(input("Selecciona el número que corresponda a la sección de tu pregunta: "))
                
                
                
    print()   
    print("Espero haber resuelto tu duda")
    #Funciona como cierre de la funcion While
                
        
        
main()
print("GitHub: https://github.com/CarMC26/Proyecto-Final-.git")
#https://github.com/CarMC26/Proyecto-Final-.git