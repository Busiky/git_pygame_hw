import math

import pygame

pygame.init()

size = width, height = 500, 500
screen = pygame.display.set_mode(size)


def draw():
    pygame.draw.rect(screen, pygame.Color('white'), (50, 20, 430, 100))
    pygame.draw.rect(screen, pygame.Color('#65350f'), (20, 20, 30, 460))

draw()

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()
