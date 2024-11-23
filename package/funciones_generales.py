# funciones.py
import pygame
import random
from package.constantes import *
from pygame import *

# Generales
def convertir_csv_a_lista_diccionarios(path:str) -> list:
    """
    ¿Que hace?-> Recibe la ruta de un csv lee sus lineas 
    y las convierte en una lista de diccionarios, 
    entre las cabezeras y cada linea
    ¿Que parametros acepta?
        -path:str -> ruta del csv
    ¿Que retorna?-> list: Una lista de diccionariosformados 
    por las cabezeras y los datos linea a linea del csv
    """
    lista_diccionarios = []
    
    with open(path, mode='r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()
        
        encabezados = lineas[0].strip().split(',')
        

        for linea in lineas[1:]:
            valores = linea.strip().split(',')

            for i in range(len(valores)):
                valores[i] = valores[i].strip('"')

            fila_diccionario = dict(zip(encabezados, valores))
            lista_diccionarios.append(fila_diccionario)
    
    return lista_diccionarios

def crear_botones(opciones: list, alto: int, ancho:int , espaciado: int) -> list:
    '''
    ¿Que hace? Recibe una lista con opciones y
      crea los botones acordes a cada elemento de la lista,
      acomodando su posición y tamaño
    ¿Que parametros acepta?
        -opciones:list -> lista con las opciones a crear botones
        -alto:int -> alto del boton a crear
        -ancho:int -> ancho del boton a crear
        -espaciado:int -> espacio entre botones
    ¿Que retorna? -> Lista de botones(tupla y texto del boton)
    '''
    botones = []
    
    # Calculo espacio total a ocupar por botones + espaciado
    espacio_total_botones = (alto + espaciado) * len(opciones)

    espacio_restante = DIMENSIONES_VENTANA[1] - espacio_total_botones
    margen_superior = espacio_restante // 2
    x_inicial = (DIMENSIONES_VENTANA[0] - ancho) // 2
    y_inicial = margen_superior

    for i in range(len(opciones)):
        # la posicion en y se calcula (alto+espacio) espacio total a ocupar por cada boton
        # y lo muliplico por el indice para evitar que se superpongan
        rect = pygame.Rect(x_inicial, y_inicial + i *(alto + espaciado), ancho, alto)
        botones.append((rect, opciones[i]))


    return botones

def dibujar_botones(ventana, botones: list, fuente):
    '''
    ¿Que hace? -> Dibuja los botones en la ventana
    ¿Que parametros acepta?
        -ventana:pygame.Surface -> Superficie donde se van 
                                    a dibujar los botones
        -botones: Lista de botones(tupla(rectangulo,texto))
        -fuente:pygame.font.Font -> fuente utilizada para los textos
    ¿Que retorna? -> None
    '''
    for rect, texto in botones:
        # rectangulo celeste
        pygame.draw.rect(ventana, AZUL_CLARO, rect)
        # borde negro
        pygame.draw.rect(ventana, NEGRO, rect, 2)

        texto_boton = fuente.render(texto, True, NEGRO)
        
        # Centra el texto en el botón
        texto_x = rect.centerx - texto_boton.get_width() // 2
        texto_y = rect.centery - texto_boton.get_height() // 2
        
        ventana.blit(texto_boton, (texto_x, texto_y))

def manejar_click_botones(botones: list) -> str|None:
    '''
    ¿Que hace? -> maneja los clicks para checkear si se clickeo en alguna botón
    ¿Que parametros acepta?
        -botones: Lista de botones(tupla(rectangulo,texto))
    ¿Que retorna?:str|None -> Si te toco un boton el texto del mismo, sino None
    '''
    pos_mouse = pygame.mouse.get_pos()
    # verifica si hay colisin de la posición del mouse con los botones
    for rect, texto in botones:
        if rect.collidepoint(pos_mouse):
            return texto
    return None

def ajustar_texto(texto: str, fuente: pygame.font.Font, ancho_maximo: int) -> list:
    '''
    ¿Qué hace?
    ¿Qué parámetros acepta?
    ¿Qué retorna?
    '''
    palabras = texto.split()
    lineas = []
    linea_actual = ""

    for palabra in palabras:
        if fuente.size(linea_actual + palabra)[0] <= ancho_maximo:
            linea_actual += palabra + " "
        else:
            lineas.append(linea_actual.strip())
            linea_actual = palabra + " "

    if linea_actual:
        lineas.append(linea_actual.strip())

    return lineas

    
