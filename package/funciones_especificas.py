import pygame
import random
from package.constantes import *
from pygame import *
from package.funciones_generales import *

#Boton para volver al menú principal
def crear_boton_menu(ventana: pygame.Surface, fuente: pygame.font.Font):
    #Botón para volver al menú
    rect_boton = pygame.Rect(BOTON_X, BOTON_Y, BOTON_ANCHO, BOTON_ALTO)
    pygame.draw.rect(ventana, AZUL_CLARO, rect_boton)
    pygame.draw.rect(ventana, NEGRO, rect_boton, 2)

    texto_renderizado = fuente.render(BOTON_TEXTO, True, NEGRO)
    texto_x = rect_boton.centerx - texto_renderizado.get_width() // 2
    texto_y = rect_boton.centery - texto_renderizado.get_height() // 2
    ventana.blit(texto_renderizado, (texto_x, texto_y))

    return rect_boton

# Pantalla de ranking
# Modificar ranking si el puntaje obtenido es mayor al menor de la lista
def dibujar_ranking(ventana: pygame.Surface, fuente: pygame.font.Font) -> pygame.rect.Rect:
    '''
    ¿Que hace? -> Dibuja la pantalla del ranking con formato de tabla
    ¿Que parametros acepta?
        -ventana:pygame.Surface -> Superficie donde se van a dibujar los botones
        -lista_ranking:list -> lista de usuarios, puntuaciones, tiempo
        -fuente:pygame.font.Font -> fuente utilizada para los textos
    ¿Que retorna?:pygame.rect.Rect -> rectángulo de pygame del botón para volver al menú principal
    '''
    lista_ranking = convertir_csv_a_lista_diccionarios('csv/ranking.csv')

    # ventana.fill(NEGRO)

    fondo = pygame.image.load("assets/fondo4.jpg")
    fondo = pygame.transform.scale(fondo, (DIMENSIONES_VENTANA))

    ventana.blit(fondo, (0, 0))

    columna_usuario_texto = fuente.render("Usuario", True, NEGRO)
    columna_puntaje_texto = fuente.render("Puntuación", True, NEGRO)
    columna_tiempo_texto = fuente.render("Tiempo", True, NEGRO)

    # Posicion de los títulos
    y_inicial = 60
    ventana.blit(columna_usuario_texto,
                 (DIMENSIONES_VENTANA[0] // 4 - columna_usuario_texto.get_width() // 2, y_inicial))
    ventana.blit(columna_puntaje_texto,
                 (DIMENSIONES_VENTANA[0] // 2 - columna_puntaje_texto.get_width() // 2, y_inicial))
    ventana.blit(columna_tiempo_texto, (3 *
                 DIMENSIONES_VENTANA[0] // 4 - columna_tiempo_texto.get_width() // 2, y_inicial))

    # Linea blanca
    pygame.draw.line(ventana, NEGRO, (50, y_inicial + 30),
                     (DIMENSIONES_VENTANA[0] - 50, y_inicial + 30), 2)

    # Espacio para las filas
    y_inicial += 40

    for i, entrada in enumerate(lista_ranking):
        texto_usuario = fuente.render(entrada['usuario'], True, NEGRO)
        texto_puntaje = fuente.render(str(entrada['puntaje']), True, NEGRO)
        texto_tiempo = fuente.render(str(entrada['tiempo']), True, NEGRO)

        # Posición de la columna
        ventana.blit(
            texto_usuario, (DIMENSIONES_VENTANA[0] // 4 - texto_usuario.get_width() // 2, y_inicial + i * 40))
        ventana.blit(
            texto_puntaje, (DIMENSIONES_VENTANA[0] // 2 - texto_puntaje.get_width() // 2, y_inicial + i * 40))
        ventana.blit(
            texto_tiempo, (3 * DIMENSIONES_VENTANA[0] // 4 - texto_tiempo.get_width() // 2, y_inicial + i * 40))

    #Botón para volver al menú
    respuesta_boton_volver_menu_principal = crear_boton_menu(ventana, fuente)
    return respuesta_boton_volver_menu_principal

# Pantalla de configuraciones
def dibujar_configuraciones(ventana: pygame.Surface, fuente: pygame.font.Font) -> pygame.rect.Rect:
    '''
    ¿Qué hace?
    ¿Qué parámetros acepta?
    ¿Qué retorna?
    '''

    # ventana.fill(NEGRO)

    fondo = pygame.image.load("assets/fondo4.jpg")
    fondo = pygame.transform.scale(fondo, (DIMENSIONES_VENTANA))

    ventana.blit(fondo, (0, 0))

    titulo_texto = fuente.render("Configuraciones", True, NEGRO)
    titulo_x = (DIMENSIONES_VENTANA[0] - titulo_texto.get_width()) // 2
    ventana.blit(titulo_texto, (titulo_x, 20))

    opciones = ["Cambiar dificultad", "Cambiar puntaje", "Cambiar tiempo"]
    botones = crear_botones(opciones, 50, 320, 20)

    dibujar_botones(ventana, botones, fuente)

    #Botón para volver al menú
    respuesta_boton_volver_menu_principal = crear_boton_menu(ventana, fuente)
    return respuesta_boton_volver_menu_principal


# Pantalla de la partida
# Pedir nombre al usuario
def pedir_nombre_usuario(ventana: pygame.Surface, fuente: pygame.font.Font, puntaje: int, cantidad_preguntas):
    # Solicitar nombre al usuario
    nombre_ingresado = ""
    bandera_pedir_nombre = True

    while bandera_pedir_nombre:

        ventana.fill(NEGRO)
        # Mostrar puntaje final
        resultado_texto = fuente.render(f"Puntaje final: {puntaje}/{cantidad_preguntas}", True, BLANCO)
        ventana.blit(resultado_texto, (DIMENSIONES_VENTANA[0] // 2 - resultado_texto.get_width() // 2, (DIMENSIONES_VENTANA[1] // 3 - 50)))

        mensaje = fuente.render("Ingrese su nombre:", True, BLANCO)
        ventana.blit(mensaje, (DIMENSIONES_VENTANA[0] // 2 - mensaje.get_width() // 2, DIMENSIONES_VENTANA[1] // 3))

        nombre_texto = fuente.render(nombre_ingresado, True, VERDE_MANZANA)
        ventana.blit(nombre_texto, (DIMENSIONES_VENTANA[0] // 2 - nombre_texto.get_width() // 2, DIMENSIONES_VENTANA[1] // 2))

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    bandera_pedir_nombre = False
                elif evento.key == pygame.K_BACKSPACE:
                    nombre_ingresado = nombre_ingresado[:-1]
                else:
                    nombre_ingresado += evento.unicode

    return nombre_ingresado

def buscar_menor_puntaje_ranking(lista: list) -> int:
    '''
    '''
    min_valor = int(lista[0]['puntaje'])
    indice_menor_valor = 0

    for i in range(1, len(lista)):
        if int(lista[i]['puntaje']) < min_valor:
            min_valor = int(lista[i]['puntaje'])
            indice_menor_valor = i

    return indice_menor_valor

def modificar_ranking(datos_jugador: dict):
    '''
    '''
    lista = convertir_csv_a_lista_diccionarios('csv/ranking.csv')
    indice = buscar_menor_puntaje_ranking(lista)
    datos = lista[indice]

    if int(datos_jugador['puntaje']) > int(datos['puntaje']):
        lista[indice] = datos_jugador
    elif (int(datos_jugador['puntaje']) == int(datos['puntaje']) and 
          int(datos_jugador['tiempo']) < int(datos['tiempo'])):
        lista[indice] = datos_jugador

    lista = ordenar_lista_diccionarios(lista)
    convertir_lista_diccionarios_a_csv(lista,'csv/ranking.csv')

def dibujar_partida(ventana: pygame.Surface, fuente: pygame.font.Font) -> pygame.rect.Rect:
    '''
    ¿Qué hace?
    ¿Qué parámetros acepta?
    ¿Qué retorna?
    '''

    preguntas = lista_preguntas = convertir_csv_a_lista_diccionarios("csv/preguntas.csv")
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

        # fondo = pygame.image.load("assets/fondo-preguntas.jpg")
        # fondo = pygame.transform.scale(fondo, (DIMENSIONES_VENTANA))

        # ventana.blit(fondo, (0, 0))

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

    nombre_usuario = pedir_nombre_usuario(ventana,fuente,puntaje,len(preguntas))
    datos_jugador = {'usuario': nombre_usuario,'puntaje': str(puntaje), 'tiempo': str(30)}
    #Verifico si el puntaje obtenido es mayor al menor del ranking
    modificar_ranking(datos_jugador)

    # Botón para volver al menú
    respuesta_boton_volver_menu_principal = crear_boton_menu(ventana, fuente)

    pygame.display.flip()

    
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
            if evento.type == pygame.MOUSEBUTTONDOWN and respuesta_boton_volver_menu_principal.collidepoint(evento.pos):
                return respuesta_boton_volver_menu_principal


