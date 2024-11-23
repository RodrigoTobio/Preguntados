import pygame
import random
from package.constantes import *
from pygame import *
from package.funciones_generales import *

# Pantalla de ranking
def dibujar_ranking(ventana: pygame.Surface, lista_ranking: list, fuente: pygame.font.Font) -> pygame.rect.Rect:
    '''
    ¿Que hace? -> Dibuja la pantalla del ranking con formato de tabla
    ¿Que parametros acepta?
        -ventana:pygame.Surface -> Superficie donde se van a dibujar los botones
        -lista_ranking:list -> lista de usuarios, puntuaciones, tiempo
        -fuente:pygame.font.Font -> fuente utilizada para los textos
    ¿Que retorna?:pygame.rect.Rect -> rectángulo de pygame del botón para volver al menú principal
    '''

    ventana.fill(NEGRO)

    # fondo = pygame.image.load("assets/fondo5.jpg")
    # fondo = pygame.transform.scale(fondo, (DIMENSIONES_VENTANA))

    # ventana.blit(fondo, (0, 0))

    columna_usuario_texto = fuente.render("Usuario", True, BLANCO)
    columna_puntaje_texto = fuente.render("Puntuación", True, BLANCO)
    columna_tiempo_texto = fuente.render("Tiempo", True, BLANCO)

    # Posicion de los títulos
    y_inicial = 60
    ventana.blit(columna_usuario_texto,
                 (DIMENSIONES_VENTANA[0] // 4 - columna_usuario_texto.get_width() // 2, y_inicial))
    ventana.blit(columna_puntaje_texto,
                 (DIMENSIONES_VENTANA[0] // 2 - columna_puntaje_texto.get_width() // 2, y_inicial))
    ventana.blit(columna_tiempo_texto, (3 *
                 DIMENSIONES_VENTANA[0] // 4 - columna_tiempo_texto.get_width() // 2, y_inicial))

    # Linea blanca
    pygame.draw.line(ventana, BLANCO, (50, y_inicial + 30),
                     (DIMENSIONES_VENTANA[0] - 50, y_inicial + 30), 2)

    # Espacio para las filas
    y_inicial += 40

    for i, entrada in enumerate(lista_ranking):
        texto_usuario = fuente.render(entrada['usuario'], True, BLANCO)
        texto_puntaje = fuente.render(str(entrada['puntaje']), True, BLANCO)
        texto_tiempo = fuente.render(str(entrada['tiempo']), True, BLANCO)

        # Posición de la columna
        ventana.blit(
            texto_usuario, (DIMENSIONES_VENTANA[0] // 4 - texto_usuario.get_width() // 2, y_inicial + i * 40))
        ventana.blit(
            texto_puntaje, (DIMENSIONES_VENTANA[0] // 2 - texto_puntaje.get_width() // 2, y_inicial + i * 40))
        ventana.blit(
            texto_tiempo, (3 * DIMENSIONES_VENTANA[0] // 4 - texto_tiempo.get_width() // 2, y_inicial + i * 40))

    boton_texto = "Volver al Menú"
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

    return rect_boton

# Pantalla de configuraciones
def dibujar_configuraciones(ventana: pygame.Surface, fuente: pygame.font.Font) -> pygame.rect.Rect:
    '''
    ¿Qué hace?
    ¿Qué parámetros acepta?
    ¿Qué retorna?
    '''

    ventana.fill(NEGRO)

    titulo_texto = fuente.render("Configuraciones", True, NEGRO)
    titulo_x = (DIMENSIONES_VENTANA[0] - titulo_texto.get_width()) // 2
    ventana.blit(titulo_texto, (titulo_x, 20))

    opciones = ["Cambiar dificultad", "Cambiar puntaje", "Cambiar tiempo"]
    botones = crear_botones(opciones, 50, 320, 20)

    dibujar_botones(ventana, botones, fuente)

    boton_texto = "Volver al Menú"
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

    return rect_boton

# Pantalla de la partida
def dibujar_partida(ventana: pygame.Surface, preguntas: list, fuente: pygame.font.Font) -> pygame.rect.Rect:
    '''
    ¿Qué hace?
    ¿Qué parámetros acepta?
    ¿Qué retorna?
    '''
    random.shuffle(preguntas)

    puntaje = 0
    indice_pregunta = 0

    # Margen costado
    ancho_maximo_texto = DIMENSIONES_VENTANA[0] - 100

    while indice_pregunta < len(preguntas):
        pregunta_actual = preguntas[indice_pregunta]
        pregunta = pregunta_actual['pregunta']
        opciones = pregunta_actual['opciones'].split(';')
        respuesta_correcta = pregunta_actual['respuesta_correcta']

        # Ajustar la pregunta si es muy larga divide en varias lineas
        lineas_pregunta = ajustar_texto(pregunta, fuente, ancho_maximo_texto)

        ventana.fill(NEGRO)

        # Pregunta
        y_actual = 50
        for linea in lineas_pregunta:
            texto_pregunta = fuente.render(linea, True, BLANCO)
            ventana.blit(texto_pregunta, (DIMENSIONES_VENTANA[0] // 2 - texto_pregunta.get_width() // 2, y_actual))
            y_actual += texto_pregunta.get_height() + 10

        # Opciones
        botones_opciones = crear_botones(
            opciones, DIMENSIONES_BOTONES_MENU_PRINCIPAL[1], DIMENSIONES_BOTONES_MENU_PRINCIPAL[0], DIMENSIONES_BOTONES_MENU_PRINCIPAL[2])
        dibujar_botones(ventana, botones_opciones, fuente)

        pygame.display.flip()

        # Espera respuesta
        respuesta_usuario = None
        while respuesta_usuario is None:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    respuesta_usuario = manejar_click_botones(botones_opciones)

        # Verifica si es correcta
        if respuesta_usuario == respuesta_correcta:
            puntaje += 1

        indice_pregunta += 1

    # Mostrar puntaje final
    ventana.fill(NEGRO)
    resultado_texto = fuente.render(f"Puntaje final: {puntaje}/{len(preguntas)}", True, BLANCO)
    ventana.blit(resultado_texto, (DIMENSIONES_VENTANA[0] // 2 -
                 resultado_texto.get_width() // 2, DIMENSIONES_VENTANA[1] // 3))

    # Botón para volver al menú
    boton_texto = "Volver al Menú"
    boton_ancho = 300
    boton_alto = 50
    boton_x = (DIMENSIONES_VENTANA[0] - boton_ancho) // 2
    boton_y = DIMENSIONES_VENTANA[1] // 2

    rect_boton = pygame.Rect(boton_x, boton_y, boton_ancho, boton_alto)
    pygame.draw.rect(ventana, AZUL_CLARO, rect_boton)
    pygame.draw.rect(ventana, NEGRO, rect_boton, 2)

    texto_renderizado = fuente.render(boton_texto, True, NEGRO)
    texto_x = rect_boton.centerx - texto_renderizado.get_width() // 2
    texto_y = rect_boton.centery - texto_renderizado.get_height() // 2
    ventana.blit(texto_renderizado, (texto_x, texto_y))

    pygame.display.flip()

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
            if evento.type == pygame.MOUSEBUTTONDOWN and rect_boton.collidepoint(evento.pos):
                return rect_boton
