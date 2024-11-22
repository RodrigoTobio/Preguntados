# funciones.py
import pygame
from constantes import *

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
    print(opciones)
    botones = []
    
    # Calculo espacio total a ocupar por botones + espaciado
    espacio_total_botones = (alto + espaciado) * len(opciones)

    espacio_restante = DIMENSIONES_VENTANA[1] - espacio_total_botones
    margen_superior = espacio_restante // 2
    x_inicial = (DIMENSIONES_VENTANA[0] - ancho) // 2
    y_inicial = margen_superior
    

    for i, texto in enumerate(opciones):
        print(i)
        # la posicion en y se calcula (alto+espacio) espacio total a ocupar por cada boton 
        # y lo muliplico por el indice para evitar que se superpongan
        rect = pygame.Rect(x_inicial, y_inicial + i * (alto + espaciado), ancho, alto)
        botones.append((rect, texto))

    print(botones[0])
    print(type(botones[0]))

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

        # texto del botón
        texto_renderizado = fuente.render(texto, True, NEGRO)
        
        # Centra el texto en el botón
        texto_x = rect.centerx - texto_renderizado.get_width() // 2
        texto_y = rect.centery - texto_renderizado.get_height() // 2
        
        ventana.blit(texto_renderizado, (texto_x, texto_y))

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


def dibujar_ranking(ventana: pygame.Surface, lista_ranking: list, fuente: pygame.font.Font):
    '''
    ¿Que hace? -> Dibuja la pantalla del ranking
    ¿Que parametros acepta?
        -ventana:pygame.Surface -> Superficie donde se van 
                                    a dibujar los botones
        -lista_ranking:list -> lista de usuarios,puntuaciones,tiempo
        -fuente:pygame.font.Font -> fuente utilizada para los textos
    ¿Que retorna?:pygame.rect.Rect -> rectangulo de pygame del boton para
                                        volver al menú principal
    '''

    ventana.fill(NEGRO)

    titulo_texto = fuente.render("Ranking", True, BLANCO)
    titulo_x = (DIMENSIONES_VENTANA[0] - titulo_texto.get_width()) // 2
    ventana.blit(titulo_texto, (titulo_x, 20))

    y_inicial = 120
    for i, entrada in enumerate(lista_ranking):
        texto = f"{i + 1}. {entrada['usuario']} - {entrada['puntaje']} - {entrada['tiempo']}"
        texto_renderizado = fuente.render(texto, True, BLANCO)
        texto_x = (DIMENSIONES_VENTANA[0] - texto_renderizado.get_width()) // 2
        ventana.blit(texto_renderizado, (texto_x, y_inicial + i * 40))

    boton_texto = "Volver al Menú Principal"
    boton_ancho = 300
    boton_alto = 50
    boton_x = (DIMENSIONES_VENTANA[0] - boton_ancho) // 2
    boton_y = DIMENSIONES_VENTANA[1] - boton_alto - 20

    rect_boton = pygame.Rect(boton_x, boton_y, boton_ancho, boton_alto)
    pygame.draw.rect(ventana, AZUL_CLARO, rect_boton)
    pygame.draw.rect(ventana, NEGRO, rect_boton, 2)

    texto_renderizado = fuente.render(boton_texto, True, NEGRO)
    texto_x = rect_boton.centerx - texto_renderizado.get_width() // 2
    texto_y = rect_boton.centery - texto_renderizado.get_height() // 2
    ventana.blit(texto_renderizado, (texto_x, texto_y))

    print(type(rect_boton))
    return rect_boton