# set image path im a variable
background_image_filename = 'Images/voldemort_4.jpg'
mouse_image_file_name = 'Images/superman 5.jpg'

# import pygame module

import pygame
import pygame.locals
from sys import exit

# it initializes each of the submodules in the pygame package
pygame.init()
# print(pygame.init())

# set screen size (width , height)
# next parameter is for set_mode, it is a flag, flag is a feature
# that can be switch on or off, it can be  combine several flags with the bitwise OR (|)
# 
screen = pygame.display.set_mode((880, 640), 0, 32)
# display caption
pygame.display.set_caption("Hello World pygame")

# set background image and convert in gray scale
background = pygame.image.load(background_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_file_name).convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == 'QUIT':
            pygame.quit()
            exit()

        screen.blit(background, (0, 0))

        x, y = pygame.mouse.get_pos()
        x -= mouse_cursor.get_width() / 2
        y -= mouse_cursor.get_height() / 2
        screen.blit(mouse_cursor, (x, y))

        pygame.display.update()
