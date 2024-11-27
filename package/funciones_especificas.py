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

    ventana.fill(NEGRO)

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
def filtrar_preguntas_por_dificultad(dificultad: str):
    preguntas = convertir_csv_a_lista_diccionarios("csv/preguntas.csv")
    preguntas_filtradas = []
    for pregunta in preguntas[1:]:
        if pregunta['dificultad'] == dificultad:
            preguntas_filtradas.append(pregunta)

    return preguntas_filtradas


def pedir_nombre_usuario(ventana: pygame.Surface, fuente: pygame.font.Font, cantidad_respuestas_correctas: int, total: int):
    '''
    '''
    nombre_ingresado = ""
    bandera_pedir_nombre = True

    while bandera_pedir_nombre:

        ventana.fill(NEGRO)
        # Mostrar puntaje final
        resultado_texto = fuente.render(f"Puntaje final: {cantidad_respuestas_correctas}/{total}", True, BLANCO)
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
        elif int(lista[i]['puntaje']) == min_valor:
            if indice_menor_valor > i:
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
    '''
    configuraciones = convertir_csv_a_lista_diccionarios('csv/configuraciones.csv')
    dificultad = configuraciones[0]['valor_elegido'].strip("'")
    puntaje_por_acierto = int(configuraciones[1]['valor_elegido'])
    tiempo_por_pregunta = int(configuraciones[2]['valor_elegido'])

    preguntas = filtrar_preguntas_por_dificultad(dificultad)
    random.shuffle(preguntas)

    correctas = 0
    indice_pregunta = 0
    tiempo_utilizado = 0

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
        botones_opciones = crear_botones(opciones, DIMENSIONES_BOTONES_MENU_PRINCIPAL[1],
                                          DIMENSIONES_BOTONES_MENU_PRINCIPAL[0], DIMENSIONES_BOTONES_MENU_PRINCIPAL[2])
        dibujar_botones(ventana, botones_opciones, fuente)

        pygame.display.flip()

        # Configuración del temporizador
        tiempo_restante = 10
        tiempo_inicio = pygame.time.get_ticks()

        respuesta_usuario = None
        while respuesta_usuario == None and tiempo_restante > 0:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    respuesta_usuario = manejar_click_botones(botones_opciones)

            # Actualizar el contador de tiempo
            tiempo_maximo = tiempo_por_pregunta
            tiempo_actual = pygame.time.get_ticks()
            tiempo_restante = max(0, tiempo_maximo - (tiempo_actual - tiempo_inicio) // 1000)

            # Limpiar el área del temporizador
            rect_tiempo = pygame.Rect(DIMENSIONES_VENTANA[0] - 150, 10, 140, 30)  # Ajusta el tamaño según el texto
            pygame.draw.rect(ventana, NEGRO, rect_tiempo)  # Rellena con el color de fondo

            # Dibujar el temporizador en la esquina superior derecha
            texto_tiempo = fuente.render(f"{tiempo_restante}", True, BLANCO)
            ventana.blit(texto_tiempo, (DIMENSIONES_VENTANA[0] - texto_tiempo.get_width() - 20, 10))

            pygame.display.update(rect_tiempo)


        # Calcular el tiempo utilizado para esta pregunta
        tiempo_usado = (pygame.time.get_ticks() - tiempo_inicio) // 1000
        tiempo_utilizado += tiempo_usado  # Sumar al total

        # Verifica si es correcta
        if respuesta_usuario == respuesta_correcta:
            correctas += 1

        indice_pregunta += 1

    nombre_usuario = pedir_nombre_usuario(ventana, fuente, correctas, len(preguntas))

    puntaje_jugador = correctas * puntaje_por_acierto
    datos_jugador = {'usuario': nombre_usuario, 'puntaje': str(puntaje_jugador), 'tiempo': str(tiempo_utilizado)}
    
    # Verifico si el puntaje obtenido es mayor al menor del ranking
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
