#!/usr/bin/env python
import sys
import pygame
from pygame.locals import *
from state import State
from cell import Cell

state = State(dimensions=(500,500))
pygame.init()
screen = pygame.display.set_mode(state.dimensions)
pygame.display.set_caption("Cauto")
#screen = pygame.display.get_surface().convert()

clock = pygame.time.Clock()
rate = 10 # Initial rate

def handle_events():
    global rate
    global state
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == KEYUP:
            if event.key == 275:
                rate += 5
            elif event.key == 276:
                rate -= 5
                if rate < 0:
                    rate = 0
            elif event.key == 27:
                exit()
            print "Simulating at %s fps" % rate
        elif event.type == MOUSEBUTTONDOWN:
             state.cells.append(Cell(event.pos))
             
def exit():
    pygame.quit()
    sys.exit(0)

while True:
    # Limits simulation frame rate
    clock.tick(rate)
    print clock.get_fps()

    # Handle events
    handle_events()
    while rate==0:
        handle_events()

    screen.fill(pygame.Color("white"))
    # First, draw map
    for a  in range(len(state.themap.grid)):
	for b in range(len(state.themap.grid[a])):
	    pygame.draw.rect(screen, (100,100+state.themap.grid[a][b]*145,100),pygame.Rect(a*state.themap.cell_width,b*state.themap.cell_height,(a*state.themap.cell_width)+state.themap.cell_width,(b*state.themap.cell_height)+state.themap.cell_height),0)

    # Second, draw cells
    for cell in state.cells:
        pygame.draw.circle(screen, (255-cell.age*10,255-cell.age*10,255-cell.age*10), cell.position, cell.radius)
        pygame.draw.circle(screen, pygame.Color(int(cell.health*2),0,0), cell.position, cell.radius, 2)
    
    pygame.display.flip()
    state.next()