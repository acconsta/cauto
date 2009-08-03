#!/usr/bin/env python
import sys

import pygame
from pygame.locals import *
from state import State

state = State()
pygame.init()
screen = pygame.display.set_mode(state.dimensions)
pygame.display.set_caption("Cauto")
#screen = pygame.display.get_surface().convert()

clock = pygame.time.Clock()

while True:
    # Limits simulation frame rate
    clock.tick(100)

    # Exit on window close
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
#		else:
#			print event

    screen.fill(pygame.Color("white"))
    for cell in state.cells:
        pygame.draw.circle(screen, pygame.Color("purple"), cell.position, cell.radius)
        pygame.draw.circle(screen, pygame.Color("red"), cell.position, cell.radius, 1)
    pygame.display.flip()
    state.next()