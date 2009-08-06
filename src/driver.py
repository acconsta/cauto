#!/usr/bin/env python
import sys
import pygame
from pygame.locals import *
from state import State
from cell import Cell
from disc import Disc

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
        elif event.type == KEYDOWN:
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
            if event.button == 1:
                state.cells.append(Cell(event.pos))
                cell = state.cells[-1]
                # Draw the cell immediately
                pygame.draw.circle(screen, (255-(cell.age*10),255-(cell.age*10),255-(cell.age*10)), cell.position, cell.radius)
                pygame.display.update(pygame.draw.circle(screen, (cell.health *2.5, cell.health *2.5, cell.health *2.5), cell.position, cell.radius, 4))
            elif event.button == 3:
                state.discs.append(Disc(event.pos))
                disc = state.discs[-1]
             
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
    screen.fill((50, 195, 50))
    for a in xrange(len(state.themap.grid)):
        for b in xrange(len(state.themap.grid[a])):
            if state.themap.grid[b][a][0] != 1:
                screen.fill((50,50+state.themap.grid[b][a][0]*145,50),pygame.Rect(a*state.themap.cell_width,b*state.themap.cell_height,state.themap.cell_width,state.themap.cell_height))
    
    # Second, draw antibiotic discs
    for disc in state.discs:
        color = [0, pygame.Color("red"), pygame.Color("orange"), pygame.Color("yellow")][disc.type]
        pygame.draw.circle(screen, color, disc.position, disc.radius)

    # Third, draw cells
    for cell in state.cells:
        body = (255-(cell.age*10),255-(cell.age*10),255-(cell.age*10))
        pygame.draw.circle(screen, body, cell.position, cell.radius)
        
        border = [pygame.Color("black"), pygame.Color("red"), pygame.Color("orange"), pygame.Color("yellow")][cell.dna.wall_type]
        pygame.draw.circle(screen, border, cell.position, cell.radius, 4)
    
    pygame.display.update()
    state.next()
