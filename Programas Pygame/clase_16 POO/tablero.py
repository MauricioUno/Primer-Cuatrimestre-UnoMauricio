import pygame
from constantes import *
from sonidos import *
from objetos import *

def init():
    
    tablero = Tablero()
    i = 1
    for x in range(0,CANTIDAD_TARJETAS_H*ANCHO_TARJETA,ANCHO_TARJETA):
        for y in range(0,CANTIDAD_TARJETAS_V*ALTO_TARJETA,ALTO_TARJETA):
            if(i > CANTIDAD_TARJETAS_UNICAS):
                tarjeta_test = Tarjeta("0{0}.png".format(i-CANTIDAD_TARJETAS_UNICAS), x, y)
            else:
                tarjeta_test = Tarjeta("0{0}.png".format(i), x, y)
            tablero.agregar_elemento(tarjeta_test)
            i = i + 1
            

    return tablero

def colision(tablero: Tablero, pos_xy):
    if (tablero.contar_tarjetas_visibles_no_descubiertas() < 2):
        for aux_tarjeta in tablero.lista_tarjetas:
            if aux_tarjeta.verificar_colision(pos_xy):
                sonido_voltear.play()
                aux_tarjeta.visible = True
                tablero.cambiar_tiempo(pygame.time.get_ticks())

def update(tablero: Tablero):
    
    tiempo_actual = pygame.time.get_ticks()
    if tablero.tiempo > 0 and tablero.contar_tarjetas_visibles_no_descubiertas() == 2:
        if tiempo_actual - tablero.tiempo > 500:
            tablero.comprobar_par_descubierto()
            tablero.cambiar_tiempo(0)
            for aux_tarjeta in tablero.lista_tarjetas:
                if not aux_tarjeta.descubierto:
                    aux_tarjeta.visible=False
                    
    

def render(tablero: Tablero, pantalla_juego, textos: Texto):
    
    for aux_tarjeta in tablero.lista_tarjetas:
        if(aux_tarjeta.visible):
            pantalla_juego.blit(aux_tarjeta.surface_imagen,aux_tarjeta.rect)
        else:
            pantalla_juego.blit(aux_tarjeta.surface_hide,aux_tarjeta.rect)


    pantalla_juego.blit(textos.tiempo, (0,450))

    if tablero.verificar_juego_terminado():
        tablero.verificar_musica_ganador()
        pantalla_juego.blit(textos.juego_terminado, (0,500))


    


     