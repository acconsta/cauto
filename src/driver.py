#!/usr/bin/env python
import sys
import pygame
from pygame.locals import *
from state import State

state = State()
pygame.init()
screen = pygame.display.set_mode(state.dimensions)
screen.fill(pygame.Color("white"))
pygame.display.flip()
pygame.display.set_caption("Cauto")
#screen = pygame.display.get_surface().convert()

clock = pygame.time.Clock()

rate = 1
while True:
    # Limit frame rate
    clock.tick(rate)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == KEYDOWN:
            if event.key == 275:
                rate += 5
            elif event.key == 276:
                if rate - 5 > 0:
                    rate -= 5
    state.next()
    screen.fill(pygame.Color("white"))
    for cell in state.cells:
        pygame.draw.circle(screen, pygame.Color("red"), cell.position, cell.radius)
        pygame.draw.circle(screen, pygame.Color("black"), cell.position, cell.radius, 1)
    pygame.display.flip()