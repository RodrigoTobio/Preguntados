import pygame
from package.constantes import *
from package.funciones_generales import *
from package.funciones_especificas import *
from pygame import *

pygame.init()

ventana = pygame.display.set_mode(DIMENSIONES_VENTANA)
pygame.display.set_caption("Preguntados")

fondo = pygame.image.load(RUTA_FONDO_MENU)
fondo = pygame.transform.scale(fondo, (DIMENSIONES_VENTANA))
fuente = pygame.font.Font(None, 48)

# opciones_menu_principal = ["Jugar Partida", "Ranking", "Configuración", "Estadísticas", "Agregar Pregunta", "Salir"]
opciones_menu_principal = ["Jugar Partida", "Ranking", "Configuración", "Salir"]
botones_menu_principal = crear_botones(opciones_menu_principal, DIMENSIONES_BOTONES_MENU_PRINCIPAL[1], DIMENSIONES_BOTONES_MENU_PRINCIPAL[0], DIMENSIONES_BOTONES_MENU_PRINCIPAL[2])


iniciado = True
mostrar_ranking = False
mostrar_configuraciones = False
mostrar_partida = False

while iniciado:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            iniciado = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if mostrar_ranking:
                rect_boton_volver = dibujar_ranking(ventana, fuente)
                if rect_boton_volver.collidepoint(evento.pos):
                    mostrar_ranking = False
            elif mostrar_configuraciones:
                rect_boton_volver = dibujar_configuraciones(ventana, fuente)
                if rect_boton_volver.collidepoint(evento.pos):
                    mostrar_configuraciones = False
            else:
                boton_clickeado = manejar_click_botones(botones_menu_principal)
                if boton_clickeado:
                    print(f"Has hecho clic en '{boton_clickeado}'")
                    match boton_clickeado:
                        case "Jugar Partida":
                            dibujar_partida(ventana, fuente)
                            mostrar_partida = False
                        case "Ranking":
                            mostrar_ranking = True
                        case "Configuración":
                            mostrar_configuraciones = True
                        case "Salir":
                            iniciado = False

    ventana.blit(fondo, (0, 0))

    if mostrar_ranking:
        dibujar_ranking(ventana, fuente)
    elif mostrar_configuraciones:
        dibujar_configuraciones(ventana, fuente)
    else:
        dibujar_botones(ventana, botones_menu_principal, fuente)
    
    pygame.display.flip()

pygame.quit()


