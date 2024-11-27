import pygame
import sys

# Configuración inicial
pygame.init()
ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600
COLOR_FONDO = (50, 50, 50)
COLOR_BOTON = (100, 100, 200)
COLOR_TEXTO = (255, 255, 255)
COLOR_BOTON_SELECCIONADO = (150, 150, 250)

# Variable para almacenar la dificultad seleccionada
dificultad = "Normal"  # Valor predeterminado

# Función para mostrar la pantalla de cambiar dificultad
def pantalla_cambiar_dificultad():
    global dificultad  # Indicamos que modificaremos la variable global
    pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
    pygame.display.set_caption("Cambiar Dificultad")

    fuente = pygame.font.Font(None, 40)
    botones = [
        {"texto": "Fácil", "rect": pygame.Rect(300, 150, 200, 50)},
        {"texto": "Normal", "rect": pygame.Rect(300, 250, 200, 50)},
        {"texto": "Difícil", "rect": pygame.Rect(300, 350, 200, 50)},
    ]

    corriendo = True
    while corriendo:
        pantalla.fill(COLOR_FONDO)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                for boton in botones:
                    if boton["rect"].collidepoint(evento.pos):
                        dificultad = boton["texto"]  # Actualizamos la dificultad
                        print(f"Dificultad seleccionada: {dificultad}")  # Para verificar

        # Dibujamos los botones
        for boton in botones:
            color = (
                COLOR_BOTON_SELECCIONADO
                if boton["texto"] == dificultad
                else COLOR_BOTON
            )
            pygame.draw.rect(pantalla, color, boton["rect"])
            texto_boton = fuente.render(boton["texto"], True, COLOR_TEXTO)
            texto_rect = texto_boton.get_rect(center=boton["rect"].center)
            pantalla.blit(texto_boton, texto_rect)

        pygame.display.flip()
