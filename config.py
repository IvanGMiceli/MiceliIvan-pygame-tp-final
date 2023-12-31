import pygame
from player import *
from constantes import *
from auxiliar import *
from plataforma import *
from enemigo import *


def configurar_nivel_uno(ancho_ventana, alto_ventana, tamaño_bloque):
    """
    La función "configurar_nivel_dos" establece las configuraciones para el nivel dos de un juego,
    incluyendo el fondo, plataformas, frutas, enemigos y coordenadas para sierras.
    
    :param ancho_ventana: El parámetro "ancho_ventana" representa el ancho de la ventana en píxeles
    :param alto_ventana: El parámetro "alto_ventana" representa la altura de la ventana o pantalla en
    píxeles
    :param o_bloque: El parámetro "o_bloque" no está definido en el código que proporcionaste. Parece
    ser un error tipográfico o falta una variable. Proporcione el nombre correcto del parámetro o
    proporcione más información sobre su propósito para que pueda ayudarlo más
    :return: un diccionario llamado "stage_2_configs" que contiene varias listas y coordenadas para
    configurar el nivel dos de un juego.
    """

    stage_1_configs = {"fondo": pygame.transform.scale(pygame.image.load(r"Juego\assets\Maps background\Fondo uno.png"), (ANCHO_VENTANA, ALTO_VENTANA)),
        "lista_piso" : [],
        "lista_plataformas" : [],
        "lista_plataformas_dos" : [],
        "lista_plataformas_tres" : [],
        "lista_manzanas" : [],
        "lista_kiwis" : [],
        "lista_enemigos" : []}

    for i in range(13):
        bloque = Objeto(i * tamaño_bloque,alto_ventana - tamaño_bloque,tamaño_bloque,tamaño_bloque)
        bloque.cargar_imagen_bloque(tamaño_bloque,"Terrain","Terrain.png",96,0)
        stage_1_configs["lista_piso"].append(bloque)

    for i in range(0,5):
        bloque = Objeto(i * tamaño_bloque,alto_ventana - tamaño_bloque * 3,tamaño_bloque,tamaño_bloque)
        bloque.cargar_imagen_bloque(tamaño_bloque,"Terrain","Terrain.png",96,0)
        stage_1_configs["lista_plataformas"].append(bloque)

    for i in range(0,6):
        bloque = Objeto(ancho_ventana - (tamaño_bloque * i),alto_ventana - tamaño_bloque * 4,tamaño_bloque,tamaño_bloque)
        bloque.cargar_imagen_bloque(tamaño_bloque,"Terrain","Terrain.png",96,0)
        stage_1_configs["lista_plataformas_dos"].append(bloque)

    for i in range(0,5):
        bloque = Objeto(i * tamaño_bloque,alto_ventana - tamaño_bloque * 6,tamaño_bloque,tamaño_bloque)
        bloque.cargar_imagen_bloque(tamaño_bloque,"Terrain","Terrain.png",96,0)
        stage_1_configs["lista_plataformas_tres"].append(bloque)


    for i in range(5):
        fruta = Objeto((i * tamaño_bloque) + 1, alto_ventana - tamaño_bloque * 4, 450 , 70)
        fruta.cargar_imagen_fruta(35,"Items/Fruits", "Apple.png")
        stage_1_configs["lista_manzanas"].append(fruta)

    for i in range(6):
        fruta = Objeto(ancho_ventana - (tamaño_bloque * i), alto_ventana - tamaño_bloque * 5, 450 , 70)
        fruta.cargar_imagen_fruta(35,"Items/Fruits", "Kiwi.png")
        stage_1_configs["lista_kiwis"].append(fruta)

    for i in range(3):
        stage_1_configs["lista_enemigos"].append(Enemigo((i * 2) + i * 100, ALTURA_SUELO, 50, 50, Auxiliar.cargar_sprite_sheets("Enemies", "Chicken", 32, 34, True),"derecha",1))

    coordenadas_sierras = [
        (672, ALTO_VENTANA - TAMAÑO_BLOQUE - 40, 38, 38),
        (750, ALTO_VENTANA - TAMAÑO_BLOQUE - 40, 38, 38),
        (830, ALTO_VENTANA - TAMAÑO_BLOQUE - 40, 38, 38),
    ]

    stage_1_configs["coordenadas_sierras"] = coordenadas_sierras

    return stage_1_configs

def configurar_nivel_dos(ancho_ventana, alto_ventana, tamaño_bloque):
    """
    La función "configurar_nivel_dos" establece las configuraciones para el nivel dos de un juego,
    incluyendo el fondo, plataformas, frutas, enemigos y coordenadas para sierras.
    
    :param ancho_ventana: El parámetro "ancho_ventana" representa el ancho de la ventana en píxeles
    :param alto_ventana: El parámetro "alto_ventana" representa la altura de la ventana o pantalla
    :param o_bloque: El parámetro "o_bloque" no está definido en el código que proporcionaste. Parece
    ser un error tipográfico o una variable faltante. Proporcione el nombre correcto del parámetro o
    proporcione más información sobre su propósito para que pueda ayudarlo más
    :return: un diccionario llamado "stage_2_configs" que contiene varias listas y coordenadas para
    configurar el nivel dos de un juego.
    """

    stage_2_configs = {"fondo": pygame.transform.scale(pygame.image.load(r"Juego\assets\Maps background\Fondo dos.png"), (ANCHO_VENTANA, ALTO_VENTANA)),
        "lista_piso" : [],
        "lista_plataformas" : [],
        "lista_plataformas_dos" : [],
        "lista_plataformas_tres" : [],
        "lista_bananas" : [],
        "lista_cherries" : [],
        "lista_enemigos" : []}

    for i in range(13):
        bloque = Objeto(i * tamaño_bloque,alto_ventana - tamaño_bloque,tamaño_bloque,tamaño_bloque)
        bloque.cargar_imagen_bloque(tamaño_bloque,"Terrain","Terrain.png",96,64)
        stage_2_configs["lista_piso"].append(bloque)

    for i in range(0,5):
        bloque = Objeto(i * tamaño_bloque,alto_ventana - tamaño_bloque * 3,tamaño_bloque,tamaño_bloque)
        bloque.cargar_imagen_bloque(tamaño_bloque,"Terrain","Terrain.png",96,64)
        stage_2_configs["lista_plataformas"].append(bloque)

    for i in range(0,6):
        bloque = Objeto(ancho_ventana - (tamaño_bloque * i),alto_ventana - tamaño_bloque * 4,tamaño_bloque,tamaño_bloque)
        bloque.cargar_imagen_bloque(tamaño_bloque,"Terrain","Terrain.png",96,64)
        stage_2_configs["lista_plataformas_dos"].append(bloque)

    for i in range(0,5):
        bloque = Objeto(i * tamaño_bloque,alto_ventana - tamaño_bloque * 6,tamaño_bloque,tamaño_bloque)
        bloque.cargar_imagen_bloque(tamaño_bloque,"Terrain","Terrain.png",96,64)
        stage_2_configs["lista_plataformas_tres"].append(bloque)


    for i in range(5):
        fruta = Objeto((i * tamaño_bloque) + 1, alto_ventana - tamaño_bloque * 4, 450 , 70)
        fruta.cargar_imagen_fruta(35,"Items/Fruits", "Bananas.png")
        stage_2_configs["lista_bananas"].append(fruta)

    for i in range(6):
        fruta = Objeto(ancho_ventana - (tamaño_bloque * i), alto_ventana - tamaño_bloque * 5, 450 , 70)
        fruta.cargar_imagen_fruta(35,"Items/Fruits", "Cherries.png")
        stage_2_configs["lista_cherries"].append(fruta)

    for i in range(3):
        enemigo_uno = Enemigo(0, 140, 50, 50, Auxiliar.cargar_sprite_sheets("Enemies", "Plant", 44, 42, True),"derecha")
        enemigo_dos = Enemigo(1100, 334, 50, 50, Auxiliar.cargar_sprite_sheets("Enemies", "Plant", 44, 42, True),"derecha")
        enemigo_tres = Enemigo(0, 750, 50, 50, Auxiliar.cargar_sprite_sheets("Enemies", "Plant", 44, 42, True),"derecha")
        stage_2_configs["lista_enemigos"].append(enemigo_uno)
        stage_2_configs["lista_enemigos"].append(enemigo_dos)
        stage_2_configs["lista_enemigos"].append(enemigo_tres)

    coordenadas_sierras = [
        (830, 380, 38, 38),
        (180, 480, 38, 38),
        (830, 670, 38, 38),
    ]

    stage_2_configs["coordenadas_sierras"] = coordenadas_sierras
        
    return stage_2_configs

def configurar_nivel_tres(ancho_ventana, alto_ventana, tamaño_bloque):
    """
    La función "configurar_nivel_tres" establece las configuraciones para el nivel tres de un juego,
    incluyendo fondo, plataformas, frutas y enemigos.
    
    :param ancho_ventana: El parámetro "ancho_ventana" representa el ancho de la ventana o pantalla en
    píxeles
    :param alto_ventana: El parámetro "alto_ventana" representa la altura de la ventana o pantalla
    :param o_bloque: El parámetro "o_bloque" no está definido en el código que proporcionaste. Parece
    ser un error tipográfico o una variable faltante. Proporcione el nombre del parámetro correcto o
    proporcione más información sobre lo que representa
    :return: un diccionario llamado "stage_3_configs" que contiene varias listas e imágenes para
    configurar el nivel tres de un juego.
    """

    stage_3_configs = {"fondo": pygame.transform.scale(pygame.image.load(r"Juego\assets\Maps background\Fondo tres.png"), (ANCHO_VENTANA, ALTO_VENTANA)),
        "lista_piso" : [],
        "lista_plataformas" : [],
        "lista_plataformas_dos" : [],
        "lista_plataformas_tres" : [],
        "lista_bananas" : [],
        "lista_cherries" : [],
        "lista_enemigos" : []}

    for i in range(13):
        bloque = Objeto(i * tamaño_bloque,alto_ventana - tamaño_bloque,tamaño_bloque,tamaño_bloque)
        bloque.cargar_imagen_bloque(tamaño_bloque,"Terrain","Terrain.png",96,128)
        stage_3_configs["lista_piso"].append(bloque)

    for i in range(0,5):
        bloque = Objeto(i * tamaño_bloque,alto_ventana - tamaño_bloque * 3,tamaño_bloque,tamaño_bloque)
        bloque.cargar_imagen_bloque(tamaño_bloque,"Terrain","Terrain.png",96,128)
        stage_3_configs["lista_plataformas"].append(bloque)

    for i in range(0,6):
        bloque = Objeto(ancho_ventana - (tamaño_bloque * i),alto_ventana - tamaño_bloque * 4,tamaño_bloque,tamaño_bloque)
        bloque.cargar_imagen_bloque(tamaño_bloque,"Terrain","Terrain.png",96,128)
        stage_3_configs["lista_plataformas_dos"].append(bloque)

    for i in range(0,5):
        bloque = Objeto(i * tamaño_bloque,alto_ventana - tamaño_bloque * 6,tamaño_bloque,tamaño_bloque)
        bloque.cargar_imagen_bloque(tamaño_bloque,"Terrain","Terrain.png",96,128)
        stage_3_configs["lista_plataformas_tres"].append(bloque)

    for i in range(5):
        fruta = Objeto((i * tamaño_bloque) + 1, alto_ventana - tamaño_bloque * 4, 450 , 70)
        fruta.cargar_imagen_fruta(35,"Items/Fruits", "Orange.png")
        stage_3_configs["lista_bananas"].append(fruta)

    for i in range(6):
        fruta = Objeto(ancho_ventana - (tamaño_bloque * i), alto_ventana - tamaño_bloque * 5, 450 , 70)
        fruta.cargar_imagen_fruta(35,"Items/Fruits", "Pineapple.png")
        stage_3_configs["lista_cherries"].append(fruta)

    for i in range(3):
        stage_3_configs["lista_enemigos"].append(Enemigo((i * 2) + i * 100, ALTURA_SUELO, 50, 50, Auxiliar.cargar_sprite_sheets("Enemies", "AngryPig", 36, 30, True),"derecha",2))
        
    return stage_3_configs


