# import the required pygame modules

import pygame
import sys
import pygame.locals

# initialization
# pygame.init() this function performs the initialization and needs to be
# called before any other pygame functions are called
pygame.init()
size = (400, 300)
# creates a surface object to draw on
screen = pygame.display.set_mode(size)

# caption
pygame.display.set_caption("Pygame1")

# the main loop
while True:
    sys_font = pygame.font.SysFont("Calibre", 19)
    rendered = sys_font.render("Hello Pygame", 0, (255, 100, 100))
    # this function draws on a surface
    screen.blit(rendered, (100, 100))

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            # this function cleans up resources used by pygame
            pygame.quit()
            sys.exit()
    # refresh the surface
    pygame.display.update()