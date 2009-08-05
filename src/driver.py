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

    # Handle events
    handle_events()
    while rate==0:
        handle_events()

    # First, draw map
    screen.fill((100, 245, 100))
    for a  in xrange(len(state.themap.grid)):
        for b in xrange(len(state.themap.grid[a])):
            if state.themap.grid[b][a][0] != 1:
                screen.fill((100,100+state.themap.grid[b][a][0]*145,100),pygame.Rect(a*state.themap.cell_width,b*state.themap.cell_height,state.themap.cell_width,state.themap.cell_height))

    # Second, draw cells
    for cell in state.cells:
        pygame.draw.circle(screen, (cell.dna.toxin_type*75,cell.dna.toxin_strength,255), cell.position, cell.radius)
        pygame.draw.circle(screen, (cell.dna.wall_type*75,cell.dna.wall_width*255,255), cell.position, cell.radius, 4)
    
    pygame.display.flip()
    state.next()
