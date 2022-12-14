from data_pokemones import lista_pokemones

# 01.1
def obtener_nombre_pokemon(pokemon: dict) -> str:
    '''
    Recibe como parametro un diccionario con los datos del pokemon

    Se declara un string mostrando el nombre del pokemon

    Se retorna ese string
    
    '''
    nombre_pokemon = str(pokemon["nombre"])

    return nombre_pokemon



# 01.2 
def imprimir_pokemones(pokemones: list):
    '''
    Recibe como parametro la lista de todos los pokemones y sus datos

    Recorre la lista e imprime el nombre del pokemon correspondiente
    '''
    for pokemon in pokemones:
        nombre_pokemon = obtener_nombre_pokemon(pokemon)
        mensaje_nombre = "Nombre: {0}".format(nombre_pokemon)
        print(mensaje_nombre)



# 02.1
def tiene_id_par(pokemon: dict) -> bool:
    '''
    Recibe como parametro un diccionario con los datos del pokemon

    En caso de que el 'id' del pokemon sea par, retorna True, caso contrario False
    
    '''
    es_par = False
    if(pokemon["id"] % 2 == 0):
        es_par = True    
    
    return es_par

# 02.2
def obtener_id_pokemon(pokemon: dict) -> str:
    '''
    Recibe como parametro un diccionario con los datos del pokemon

    Se declara un string mostrando el id del pokemon

    Se retorna ese string
    
    '''
    id_pokemon = str(pokemon["id"])

    return id_pokemon

# 02.3
def imprimir_pokedex_id_par(pokemones: list):
    '''
    Recibe como parametro la lista de todos los pokemones y sus datos

    Verificara si el id del pokemon es par, en caso de serlo, imprimira su nombre en pantalla

    '''
    for pokemon in pokemones:

        if tiene_id_par(pokemon):
            nombre_pokemon = obtener_nombre_pokemon(pokemon)
            id_pokemon = obtener_id_pokemon(pokemon)
            mensaje_id_par = "Nombre: {0} | ID: {1}".format(nombre_pokemon, id_pokemon)
            print(mensaje_id_par)




# 03.1
def multiplo_de_25(pokemon: dict) -> bool:
    '''
    Recibe como parametro un diccionario con los datos del pokemon

    En caso de que el 'id' del pokemon sea multiplo de 25, retorna True, caso contrario False
    
    '''
    if(pokemon["id"] % 25 == 0):
        return True
    else:
        return False


# 03.2
def imprimir_pokedex_mult_25(pokemones: list):
    '''
    Recibe como parametro la lista de todos los pokemones y sus datos

    Verificara si el id del pokemon es multiplo de 25, en caso de serlo, imprimira su nombre en pantalla

    '''
    for pokemon in pokemones:
        es_mult_25 = multiplo_de_25(pokemon)
        if es_mult_25:
            nombre_pokemon = obtener_nombre_pokemon(pokemon)
            id_pokemon = obtener_id_pokemon(pokemon)
            mensaje_mult_25 = "Nombre: {0}| ID: {1}".format(nombre_pokemon, id_pokemon)
            print(mensaje_mult_25)



# 04.1
def nombre_format_pokemon(pokemon: dict) -> str:
    '''
    Parametros:
    - Un diccionario con los datos de un pokemon

    Funcion:
    - Crea un string representando el nombre e id del pokemon (#000)

    Retorna:
    - El string creado
    '''
    nombre_pokemon = obtener_nombre_pokemon(pokemon)
    id_pokemon = int(obtener_id_pokemon(pokemon))

    entrada_pokedex = "#{0:03d} - {1}".format(id_pokemon, nombre_pokemon)
    print(entrada_pokedex)


# 04.2
def pokedex_imprimir_nombres_poke_fmt(pokemones: list):
    '''
    Parametros:
    - Lista de diccionarios con datos de pokemones

    Funcion:
    - Itera la lista de pokemones e imprime el numero y 
    nombre del pokemon en formato pokedex
    '''

    for pokemon in pokemones:
        nombre_format_pokemon(pokemon)


# 05.2