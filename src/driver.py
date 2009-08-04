#!/usr/bin/env python
import sys

import pygame
from pygame.locals import *
from state import State

state = State(dimensions=(500,500))
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
    #First, draw map
    #for a  in range(len(state.themap.grid)):
    #	for b in range(len(state.themap.grid[a])):
    #       pygame.draw.rect(screen, (255,state.themap.grid[a][b]*245,255),a+state.themap.cell_width,b+state.themap.cell_height)

    #Second, draw cells
    for cell in state.cells:
        pygame.draw.circle(screen, (255-cell.age*10,255-cell.age*10,255-cell.age*10), cell.position, cell.radius)
        pygame.draw.circle(screen, pygame.Color(int(cell.health*2),0,0), cell.position, cell.radius, 2)
    pygame.display.flip()
    state.next()