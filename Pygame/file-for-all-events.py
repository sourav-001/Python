# writing a pygame script to display all the events

# using pygame.event.wait() to wait for a single event

import pygame
import pygame.locals
from sys import exit

# initialize all of the submodules
pygame.init()

# set screensize in a variable
ScreenSize = (800, 600)  # (width, height)

# set screen
screen = pygame.display.set_mode(ScreenSize, 0, 32)

while True:
    for event in pygame.event.get():
        if event.type == 'QUIT':
            pygame.quit()
            exit()

        print(event)

    pygame.display.update()
