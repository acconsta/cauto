#!/usr/bin/env python
import pygame, sys
from pygame.locals import *
from state import *

state = State()
pygame.init()
screen = pygame.display.set_mode(state.dimensions)
pygame.display.set_caption("Cauto")
#screen = pygame.display.get_surface().convert()

clock = pygame.time.Clock()

while True:
	clock.tick(10)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit(0) 
##		else: 
##			print event
	for cell in state.cells:
		print state.time, cell.position, cell.radius
		pygame.draw.circle(screen, pygame.Color("red"), cell.position, cell.radius)
	state.next()
	pygame.display.flip()