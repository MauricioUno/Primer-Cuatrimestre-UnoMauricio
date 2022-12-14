# Uño Mauricio Ejercicio 10
import json
import re

# Punto 1.4 sin la biblioteca json
def leer_archivo_manual(nombre_archivo: str) -> list:

    with open(nombre_archivo, 'r') as archivo:
        texto_archivo = archivo.read()

    lista_nombres = re.findall('"nombre": "([a-z A-Z-]*)"', texto_archivo)
    lista_identidad = re.findall('"identidad": "([a-z A-Z()]*)"', texto_archivo)
    lista_empresa = re.findall('"empresa": "([a-z A-Z]*)"', texto_archivo)
    lista_altura = re.findall('"altura": "([0-9]+\.?[0-9]*)?"', texto_archivo)
    lista_peso = re.findall('"peso": "([0-9]+\.?[0-9]*)?"', texto_archivo)
    lista_genero = re.findall('"genero": "(M|F|NB)?"', texto_archivo)
    lista_color_ojos = re.findall('"color_ojos": "([a-z A-Z()]*)"', texto_archivo)
    lista_color_pelo = re.findall('"color_pelo": "([a-z A-Z/]*)"', texto_archivo)
    lista_fuerza = re.findall('"fuerza": "([0-9]*)"', texto_archivo)
    lista_inteligencia = re.findall('"inteligencia": "([a-z A-Z]*)"', texto_archivo)

    lista_personajes = []
    for indice in range (24):
        personaje = {}
        personaje["nombre"] = lista_nombres[indice]
        personaje["identidad"] = lista_identidad[indice]
        personaje["empresa"] = lista_empresa[indice]
        personaje["altura"] = lista_altura[indice]
        personaje["peso"] = lista_peso[indice]
        personaje["genero"] = lista_genero[indice]
        personaje["color_ojos"] = lista_color_ojos[indice]
        personaje["color_pelo"] = lista_color_pelo[indice]
        personaje["fuerza"] = lista_fuerza[indice]
        personaje["inteligencia"] = lista_inteligencia[indice]
        lista_personajes.append(personaje)


    return lista_personajes

#-----------Primera parte-----------#

# Funcion imprimir_dato
def imprimir_dato(mensaje_a_imprimir: str):
    '''
    Parametros:
    Un string

    Imprime el string
    '''
    print(mensaje_a_imprimir)
    
# Punto 1.4
def leer_archivo(nombre_archivo: str) -> list:
    '''
    Parametros:
    Un string que representa la dirección del archivo a leer

    Se carga el archivo a un diccionario cuya clave hace referencia
    a la lista de diccionario con los datos de los personajes.
    
    Se inicializa una lista y se le asigna la lista adentro del diccionario

    Retorna:
    La lista de diccionarios de los personajes
    '''
    with open(nombre_archivo, 'r') as archivo:
        diccionario = json.load(archivo)
        lista = diccionario["heroes"]

    return lista

lista_personajes = leer_archivo('Programa 10\data_stark.json')
for datos_personaje in lista_personajes:
    datos_personaje["altura"] = float(datos_personaje["altura"])
    datos_personaje["peso"] = float (datos_personaje["peso"])
    datos_personaje["fuerza"] = int (datos_personaje["fuerza"])

# Punto 1.5
def guardar_archivo(nombre_archivo: str, datos_a_guardar: str) -> bool:
    '''
    Parametros:
    Un string que representa el nombre del archivo en el que se escribira
    Un string que representa los datos que se guardaran en el archivo

    Retorna:
    True en caso de que se haya guardado con exito
    False en caso de error (Tambien imprimira un mensaje informando del error)
    '''
    archivo_guardado = False
    if re.search("(.json|.csv)$", nombre_archivo) != None:
        with open(nombre_archivo, 'w') as archivo:
            datos_guardados = archivo.write(datos_a_guardar)
            if datos_guardados == len(datos_a_guardar):
                imprimir_dato("Informacion guardada en un archivo")
                archivo_guardado = True
    else:
        imprimir_dato("El tipo de archivo no es valido")

    return archivo_guardado


# Punto 1.6
def capitalizar_palabras(string_a_capitalizar: str) -> str:
    '''
    Parametros:
    Un string

    La funcion capitalizara las palabras que encuentre en el string
    pasado como parametro

    Retorna:
    Un nuevo string con las palabras capitalizadas
    '''
    lista_palabras = set(re.findall("[a-zA-Z]+", string_a_capitalizar))

    for palabra in lista_palabras:
        palabra_capitalizada = palabra.capitalize()
        string_a_capitalizar = re.sub(palabra, palabra_capitalizada, string_a_capitalizar)


    return string_a_capitalizar


# Punto 1.7
def obtener_nombre_capitalizado(personaje: dict) -> str:
    '''
    Parametros:
    Un diccionario con los datos de un personaje

    La funcion genera un string que representa el nombre del personaje

    Retorna:
    El string generado
    '''
    nombre_capitalizado = capitalizar_palabras(personaje["nombre"])
    mensaje_nombre = "Nombre: " + nombre_capitalizado
    return mensaje_nombre


# Punto 1.8
def obtener_nombre_y_dato(personaje: dict, dato: str) -> str:
    '''
    Parametros:
    Diccionario con los datos del personaje
    String que representa una clave del diccionario (un dato del personaje)

    La funcion genera un string que representa el nombre y el dato pasado como parametro
    del personaje

    Retorna:
    El string generado
    '''
    mensaje_nombre = obtener_nombre_capitalizado(personaje)
    mensaje_dato = capitalizar_palabras(dato) + ": {}".format(personaje[dato]) 
    
    mensaje_nombre_y_dato = mensaje_nombre + " | " + mensaje_dato

    return mensaje_nombre_y_dato


#-----------Segunda parte-----------#

# Punto 2.1
def es_genero(personaje:dict, genero: str) -> bool:
    '''
    Parametros:
    - Un diccionario que contiene los datos de un personaje
    - Un string que representa el genero buscado, puede ser M, F o NB

    Retorna:
    - True en caso que el genero pasado como parametro este entre las 3 opciones
        y coincida con el genero del personaje
    - False en caso contrario
    '''
    if personaje["genero"] == genero:
        validacion_genero = True
    else:
        validacion_genero = False
    
    return validacion_genero


# Punto 2.2
def stark_imprimir_guardar_personajes_genero(personajes: list, genero_evaluar: str):
    '''
    Parametros:
    - Una lista de diccionarios con los datos de los personajes
    - El genero que se buscara en los personajes de la lista

    La funcion imprime los nombres de los personajes que sean del genero
    pasado como parametro, y despues guarda esos nombres en un archivo

    Retorna:
    - True si todo el proceso se dio sin errores
    - False si hubo un error
    '''
    archivo_guardado = False
    if re.search("^[MF]$", genero_evaluar) != None:
        lista_nombres = []
        for personaje in personajes:
            personaje_genero_elegido = es_genero(personaje, genero_evaluar)

            if personaje_genero_elegido:
                nombre_personaje = obtener_nombre_capitalizado(personaje)
                imprimir_dato(nombre_personaje)
                lista_nombres.append(nombre_personaje)
        
        if len(lista_nombres) > 0:
            mensaje_nombres = ",".join(lista_nombres)
            nombre_archivo = "personajes_{0}.csv".format(genero_evaluar)
            archivo_guardado = guardar_archivo(nombre_archivo, mensaje_nombres)
        else:
            imprimir_dato("No hay personajes del genero pasado como parametro")

    return archivo_guardado



#-----------Tercera parte-----------#

# Punto 3.1
def calcular_min_genero(personajes: list, dato: str, genero: str) -> dict:
    '''
    Parametros:
    - Lista de diccionarios con datos del personaje correspondiente
    - String 'dato', se buscara el personaje con el menor valor de esta clave
    - String 'genero' determina dentro de que genero es la busqueda del menor valor

    Determina que personaje tiene el menor valor del dato pasado como
    parametro

    Retorna:
    - El diccionario del personaje con el dato de menor valor
    '''
    flag_primer_personaje = True
    for personaje in personajes:
        if personaje["genero"] == genero:
            if flag_primer_personaje or personaje[dato] < personaje_min[dato]:
                personaje_min = personaje
                flag_primer_personaje = False

    return personaje_min


# Punto 3.2
def calcular_max_genero(personajes: list, dato: str, genero: str) -> dict: 
    '''
    Parametros:
    - Lista de diccionarios con datos del personaje correspondiente
    - String 'dato', se buscara el personaje con el mayor valor de esta clave
    - String 'genero' determina dentro de que genero es la busqueda del mayor valor

    Determina que personaje tiene el mayor valor del dato pasado como
    parametro

    Retorna:
    - El diccionario del personaje con el dato de mayor valor
    '''
    flag_primer_personaje = True
    for personaje in personajes:
        if personaje["genero"] == genero:
            if flag_primer_personaje or personaje[dato] > personaje_max[dato]:
                personaje_max = personaje
                flag_primer_personaje = False

    return personaje_max


# Punto 3.3
def calcular_max_min_dato_genero(personajes, calculo, dato, genero) -> dict:
    '''
    Parametros:
    - Lista de diccionarios con datos de los personajes
    - calculo: string que indica el tipo de calculo a realizar ('maximo' o 'minimo')
    - dato: string que hace referencia sobre que dato se realizara el calculo
    - genero: string que determina sobre que genero se realizara la busqueda del valor

    Calculara el maximo o minimo del dato pasado como parametro

    Retorna:
    - El diccionario con los datos del personaje que tiene el valor pedido
    '''
    if calculo == "maximo":
        personaje_max_min = calcular_max_genero(personajes, dato, genero)
    elif calculo == "minimo":
        personaje_max_min = calcular_min_genero(personajes, dato, genero)

    return personaje_max_min


# Punto 3.4
def stark_imprimir_guardar_max_min_genero(personajes: list, calculo: str, dato: str, genero: str) -> bool:
    '''
    Parametros:
    - Lista de diccionarios con datos de los personajes
    - calculo: string que indica el tipo de calculo a realizar ('maximo' o 'minimo')
    - dato: string que hace referencia sobre que dato se realizara el calculo
    - genero: string que determina sobre que genero se realizara la busqueda del valor

    Verifica que sea una lista con almenos un elemento, que el genero ingresado 
    sea 'M' o 'F' y que el calculo ingresado sea 'minimo' o 'maximo'.
    En caso de pasar todas las validaciones, imprime un mensaje en funcion de los
    datos pasados como parametro. Ademas, guarda ese mensaje en un archivo.

    Retorna:
    True en caso que el archivo se guarde con exito.
    False en caso de error
    '''
    archivo_guardado = False
    if type(personajes) == type([]) and len(personajes) > 0 : 
        if re.search("^[MF]$", genero) != None:
            if re.search("^(maximo|minimo)$", calculo) != None:

                personaje_max_min = calcular_max_min_dato_genero(personajes, calculo, dato, genero)
                nombre_y_dato_max_min = obtener_nombre_y_dato(personaje_max_min, dato)

                if calculo == "maximo":
                    palabra_calculo = "Mayor"
                    
                elif calculo == "minimo":
                    palabra_calculo = "Menor"

                mensaje_max_min = "{0} {1}: {2}".format(palabra_calculo, dato, nombre_y_dato_max_min)
                imprimir_dato(mensaje_max_min)

                nombre_archivo = "personajes_{0}_{1}_{2}.csv".format(calculo, dato, genero)
                archivo_guardado = guardar_archivo(nombre_archivo, mensaje_max_min)
                
    return archivo_guardado
    
#-----------Cuarta parte-----------#

# Punto 4.1
def sumar_dato_personaje_genero(personajes: list, dato: str, genero: str) -> float:
    '''
    Parametros:
    - Lista de diccionarios con los datos de los personajes
    - String 'dato'; hace referencia al dato con el que se realiza la suma
    - String 'genero'; determina sobre que genero se realiza la suma 

    Se inicializa un acumulador al que se le suma el valor del dato pasado
    como parametro, solo suma a los personajes que sean del genero pasado
    como parametro 

    Retorna:
    - El acumulador de los valores del dato pasado como parametro
    - -1 Si no se pasan todas las validaciones
    '''
    acumulador_suma_datos = 0
    for personaje in personajes:
        if type(personaje) == type({}) and personaje != {}:
            if personaje["genero"] == genero:
                acumulador_suma_datos += personaje[dato]
        else:
            acumulador_suma_datos = -1
            break

    return acumulador_suma_datos


# Punto 4.2
def cantidad_personajes_genero(personajes: list, genero: str) -> int:
    '''
    Parametros:
    - Una lista de diccionarios con los datos de los personajes
    - El genero del cual se buscara la cantidad de personajes

    La funcion iterara la lista, sumara y obtendra la cantidad de personajes
    del genero pasado como parametro

    Retorna:
    - Cantidad de personajes del genero correspondiente
    '''

    acumulador_personajes = 0
    for personaje in personajes:
        if personaje["genero"] == genero:
            acumulador_personajes += 1

    return acumulador_personajes

# Funcion dividir
def dividir(dividendo: float, divisor: int) -> float:
    '''
    Parametro:
    Un dividendo y un divisor

    Si el divisor no es cero, realizara la division

    Retorna:
    El resultado de la division
    En caso de error imprime un mensaje
    '''
    if divisor != 0 and dividendo != -1:
        resultado = dividendo / divisor
    else:
        resultado = 0
    
    return resultado


# Punto 4.3
def calcular_promedio_genero(personajes: list, dato: str, genero: str) -> float:
    '''
    Parametros:
    - Lista de diccionarios con datos de los personajes
    - String que hace referencia al dato del que se calculara el promedio
    - El genero determina sobre que grupo de personajes se buscara el promedio

    Calcula el promedio

    Retorna:
    El promedio
    '''
    acum_datos_genero = sumar_dato_personaje_genero(personajes, dato, genero)
    cant_personajes_genero = cantidad_personajes_genero(personajes, genero)
    promedio_datos = dividir(acum_datos_genero, cant_personajes_genero)

    return promedio_datos


# Punto 4.4
def stark_imprimir_guardar_promedio_altura_genero(personajes: list, genero: str) -> bool:
    '''
    Parametros:
    - Lista de diccionarios con datos del personaje correspondiente
    - El genero determina sobre que grupo de personajes se buscara el promedio de altura
    
    Verifica que sea una lista por lo menos con 1 elemento
    Obtiene el promedio de la altura de los personajes del genero 
    elegido e imprime un mensaje, luego de eso guardara el mensaje
    en un archivo.

    Retorna:
    - True si se guarda el archivo con exito
    - False si ocurre un error, ademas imprime un mensaje
    '''
    archivo_guardado = False
    if type (personajes) == type ([]) and len(personajes) > 0:
        
        promedio_altura_genero = calcular_promedio_genero(personajes, "altura", genero)
        if promedio_altura_genero != 0:
            mensaje_promedio_altura = "Altura promedio genero {0}: {1:.2f}".format(genero, promedio_altura_genero)
            imprimir_dato(mensaje_promedio_altura)

            nombre_archivo = "personajes_promedio_altura_{0}.csv".format(genero)
            archivo_guardado = guardar_archivo(nombre_archivo, mensaje_promedio_altura)
        else:
            imprimir_dato("Error al calcular el promedio de altura del genero pedido!")
    
    else:
        imprimir_dato("Error: Lista de personajes vacía!")

    return archivo_guardado



#-----------Quinta parte-----------#

# Punto 5.1
def calcular_cantidad_tipo(personajes: list, dato: str) -> dict:
    '''
    Parametros:
    - Lista de diccionarios con los datos de los personajes
    - El dato del cual se informara la cantidad de personajes por tipo

    Crea un diccionario vacio.
    Verifica si la lista tiene al menos un elemento, en caso de que asi sea,
    crea claves para el diccionario, dichas claves corresponden a los
    diferentes tipos del dato pasado como parametro.
    Luego recorre la lista de personajes incrementando el 
    valor de la clave correspondiente

    Retorna:
    - Diccionario con claves que refieren a los tipos de dato y cuyo valor refiere
      a la cantidad de personajes correspondientes a ese tipo
    - Un diccionario con una clave; "Error" y un valor un string informando que la
      lista esta vacia
    
    '''
    diccionario_tipos_de_dato = {}
    if type(personajes) == type([]) and len(personajes) > 0:
        for personaje in personajes:
            tipo = personaje[dato]
            tipo = capitalizar_palabras(tipo)
            if tipo == "":
                tipo = "N/A"
            diccionario_tipos_de_dato[tipo] = 0
        
        for personaje in personajes:
            tipo = personaje[dato]
            tipo = capitalizar_palabras(tipo)
            if tipo == "":
                tipo = "N/A"
            diccionario_tipos_de_dato [tipo] += 1
        
        for tipo in diccionario_tipos_de_dato:
            tipo = capitalizar_palabras(tipo)
    else:
        diccionario_tipos_de_dato["Error"] = "La lista se encuentra vacia"

    return diccionario_tipos_de_dato


# Punto 5.2
def guardar_cantidad_personajes_tipo(tipos_de_dato: dict, dato: str) -> bool:
    '''
    Parametros:
    - Un diccionario que tenga como claves los distintos tipos 
      del dato pasado como parametro
    - El dato del cual trata el diccionario

    La funcion crea un string que representa cada tipo de dato
    y su cantidad de personajes, para cada tipo se usa una linea.
    Luego, guarda este string en un archivo.

    Retorna:
    - True en caso de que el archivo se guarde con exito
    - False si hubo un error al guardar el archivo
    '''
    mensaje_cantidad_por_tipo = ""
    for tipo in tipos_de_dato:
        mensaje_cantidad_por_tipo += "Caracteristica: {0} {1} - Cantidad de personajes: {2}\n".format(dato, tipo, tipos_de_dato[tipo])

    nombre_archivo = "personajes_cantidad_{0}.csv".format(dato)
    archivo_guardado = guardar_archivo(nombre_archivo, mensaje_cantidad_por_tipo)

    return archivo_guardado


# Punto 5.3
def stark_calcular_guardar_cantidad_por_tipo(personajes: list, dato: str) -> bool:
    '''
    Parametros:
    - Una lista de diccionarios con los datos de los personajes
    - El dato del cual se calculara la cantidad de personajes por tipo

    Crea un diccionario que representa la cantidad de personajes por tipo 
    del dato pasado como parametro. Luego crea un string con la informacion
    de ese diccionario y lo guarda en un archivo.
    En caso de error imprime un diccionario 'error'

    Retorna:
    - True si se guardo con exito el archivo
    - False si hubo algun error
    '''
    archivo_guardado = False
    cantidad_por_tipos = calcular_cantidad_tipo(personajes, dato)
    if not ("Error" in cantidad_por_tipos.keys()):
        archivo_guardado = guardar_cantidad_personajes_tipo(cantidad_por_tipos, dato)

    else:
        imprimir_dato(cantidad_por_tipos)

    return archivo_guardado



#-----------Sexta parte-----------#

# Punto 6.1
def obtener_lista_de_tipos(personajes: list, dato: str) -> set:
    '''
    Parametros:
    - Una lista de diccionarios con los datos de los personajes
    - El dato del cual se averiguara los distintos tipos

    Crea una nueva lista, los elementos de la lista seran los distintos valores de
    la clave pasada como parametro en los diccionarios, en caso de que el dato contenga
    un valor vacio, se reemplazara por 'N/A', cada valor del diccionario se agrega
    a la nueva lista. Al final, se castea la lista a un 'set'.

    Retorna:
    - La lista seteada
    '''
    lista_tipos = []
    for personaje in personajes:
        tipo = personaje[dato]
        if tipo == "":
            tipo = "N/A"

        tipo = capitalizar_palabras(tipo)
        lista_tipos.append(tipo)

    lista_tipos = set(lista_tipos)
    
    return lista_tipos


# Punto 6.2
def normalizar_dato(valor_dato: str, valor_por_defecto: str) -> str:
    '''
    Parametros:
    - String que representa el valor de una clave de un diccionarioo
    - String que se usara en caso que el primero sea vacio

    Retorna:
    - El string valor_dato
    - El string valor_por_defecto si valor_dato es vacio
    '''
    valor_dato = valor_dato.strip()
    if len(valor_dato) > 0:
        valor_retorno = valor_dato
    else:
        valor_retorno = valor_por_defecto

    return valor_retorno


# Punto 6.3
def normalizar_personaje(personaje: dict, dato: str):
    '''
    Parametros:
    - Un diccionario con datos de un personaje
    - Una clave del diccionario que representa un dato del personaje

    Funcion:
    - Capitaliza las palabras del valor de la clave pasada como parametro
    - En caso que el valor sea vacio, lo reemplaza por 'N/A'
    - Capitaliza el nombre del personaje
    '''
    personaje[dato] = capitalizar_palabras(personaje[dato])
    personaje[dato] = normalizar_dato(personaje[dato], "N/A")

    personaje["nombre"] = capitalizar_palabras(personaje["nombre"])


# Punto 6.4
def obtener_personajes_por_tipo(personajes: list, lista_tipos: set, dato: str) -> dict:
    '''
    Parametros:
    - Lista de diccionarios con datos de los personajes
    - Una lista con los distintos tipos del dato pasado como parametro
    - El dato por el cual se clasificaran los personajes

    Funcion: 
    - Crea un diccionario vacio, se le agregan claves en funcion de lista_tipos
    - El valor de esas claves es una lista vacia
    - Se recorre la lista de personajes, se agrega los personajes a la lista de la clave correspondiente

    Retorna:
    - El diccionario con las listas de personajes segun los distintos tipos
    '''
    
    personajes_por_tipo = {}
    for tipo in lista_tipos:
        if not(tipo in personajes_por_tipo.keys()):
            personajes_por_tipo[tipo] = []
        
        for personaje in personajes:
            normalizar_personaje(personaje, dato)
            if personaje[dato] == tipo:
                personajes_por_tipo[tipo].append(personaje["nombre"])

    return personajes_por_tipo


# Punto 6.5
def guardar_heroes_por_tipo(personajes_por_tipo: dict, dato: str) -> bool:
    '''
    Parametros:
    - Un diccionario con los personajes ordenados por tipo
    - El dato por el cual se clasificaran los personajes

    Funcion:
    - Recorre el diccionario concatenando strings, cada string representa un tipo
    del dato pasado como parametro, seguido de los personajes correspondientes a ese tipo
    - Luego de recorrer el diccionario, ya se tiene el string terminado y se lo guarda
    en un archivo

    Retorna:
    - True si el archivo se guarda correctamente
    - False si hubo un error al intentar guardar el archivo
    '''
    mensaje_personajes_tipo = ""
    for tipo in personajes_por_tipo:
        personajes = " | ".join(personajes_por_tipo[tipo])
        mensaje_personajes_tipo += "Caracteristica {0} {1}: {2}\n".format(dato, tipo, personajes)

    nombre_archivo = "personajes_segun_{0}.csv".format(dato)
    archivo_guardado = guardar_archivo(nombre_archivo, mensaje_personajes_tipo)

    return archivo_guardado
        

# Punto 6.6
def stark_clasificar_guardar_personajes_por_dato(personajes: list, dato: str) -> bool:
    '''
    Parametros:
    - Una lista de diccionarios con los datos de los personajes
    - Un string que representa el dato por el cual se clasificara a los personajes

    Funcion:
    - Obtiene una lista con los distintos tipos del dato
    - Obtiene un diccionario con claves correspondientes a los distintos tipos de dato
    y su valor es la lista de los personajes pertenecientes a ese tipo
    - Genera un string que representa la clasificacion generada y lo guarda en un archivo

    Retorna:
    - True si pudo guardar el archivo
    - False caso contrario
    '''
    lista_de_tipos = obtener_lista_de_tipos(personajes, dato)
    personajes_por_tipo = obtener_personajes_por_tipo(personajes, lista_de_tipos, dato)
    archivo_guardado = guardar_heroes_por_tipo(personajes_por_tipo, dato)

    return archivo_guardado




#-----------Menu Principal-----------#

# Punto 1.1
def imprimir_menu_desafio_cinco():
    '''
    Imprime el menu de opciones
    '''
    menu_desafio = "Opciones:\
            \nA- Imprimir y guardar nombres de los personajes (género M)\
            \nB- Imprimir y guardar nombres de los personajes (género F)\
            \nC- Imprimir y guardar el personaje mas alto (género M)\
            \nD- Imprimir y guardar el personaje mas alto (género F)\
            \nE- Imprimir y guardar el personaje mas bajo (género M)\
            \nF- Imprimir y guardar el personaje mas bajo (género M)\
            \nG- Imprimir y guardar el promedio de altura (género M)\
            \nH- Imprimir y guardar el promedio de altura (género F)\
            \nI- Imprimir y guardar los personajes con mayor y menor altura (género M y F)\
            \nJ- Guardar la cantidad de personajes por cada tipo de color de ojo\
            \nK- Guardar la cantidad de personajes por cada tipo de color de pelo\
            \nL- Guardar la cantidad de personajes por cada tipo de inteligencia\
            \nM- Guardar personajes ordenados por cada tipo de color de ojo\
            \nN- Guardar personajes ordenados por cada tipo de color de pelo\
            \nO- Guardar personajes ordenados por cada tipo de inteligencia\
            \nZ- Salir"

    imprimir_dato(menu_desafio)


# Punto 1.2
def stark_menu_principal_cinco() -> str:
    '''
    Llama a la funcion imprimir_menu y pide al usuario ingresar
    una letra.

    Retorna:
    La letra ingresada
    -1 Si se ingresa algo distinto de una letra
    '''
    imprimir_menu_desafio_cinco()
    opcion_elegida = input("> ")
    if re.search("^[a-oA-OzZ]$", opcion_elegida) != None:
        opcion_elegida = opcion_elegida.upper()
        valor_retorno = opcion_elegida

    else:
        valor_retorno = -1

    return valor_retorno


# Punto 1.3
def stark_marvel_app_cinco(personajes):
    '''
    Parametros:
    Una lista de diccionarios con los datos de los personajes

    Llama a la funcion stark_menu_principal.
    En funcion de la opcion elegida, se llamaran a distintas funciones
    '''
    while True:
        opcion_elegida = stark_menu_principal_cinco()

        match (opcion_elegida):
            case "A":
                stark_imprimir_guardar_personajes_genero(personajes, "M")
            case "B":
                stark_imprimir_guardar_personajes_genero(personajes, "F")
            case "C":
                stark_imprimir_guardar_max_min_genero(personajes, "maximo", "altura", "M")
            case "D":
                stark_imprimir_guardar_max_min_genero(personajes, "maximo", "altura", "F")
            case "E":
                stark_imprimir_guardar_max_min_genero(personajes, "minimo", "altura", "M")
            case "F":
                stark_imprimir_guardar_max_min_genero(personajes, "minimo", "altura", "F")
            case "G":
                stark_imprimir_guardar_promedio_altura_genero(personajes, "M")
            case "H":
                stark_imprimir_guardar_promedio_altura_genero(personajes, "F")
            case "I":
                imprimir_dato("La funcion para esta opcion aun no fue implementada, perdon!")
            case "J":
                stark_calcular_guardar_cantidad_por_tipo(personajes, "color_ojos")
            case "K":
                stark_calcular_guardar_cantidad_por_tipo(personajes, "color_pelo")
            case "L":
                stark_calcular_guardar_cantidad_por_tipo(personajes, "inteligencia")
            case "M":
                stark_clasificar_guardar_personajes_por_dato(personajes, "color_ojos")
            case "N":
                stark_clasificar_guardar_personajes_por_dato(personajes, "color_pelo")
            case "O":
                stark_clasificar_guardar_personajes_por_dato(personajes, "inteligencia")
            case "Z":
                imprimir_dato("Adios!")
                break
            case -1:
                imprimir_dato("Ingrese una opción valida!")


stark_marvel_app_cinco(lista_personajes)