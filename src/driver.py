#!/usr/bin/env python
from sys import exit
from random import randint
import pygame
from pygame.locals import *
from state import State
from cell import Cell
from dna import DNA
from disc import Disc

pygame.font.init()
font = pygame.font.Font(None, 20)

state = State(dimensions=(500,500))
pygame.init()
screen = pygame.display.set_mode(state.dimensions)
pygame.display.set_caption("Cauto")
#screen = pygame.display.get_surface().convert()

clock = pygame.time.Clock()
rate = 10 # Initial rate

cursor_type = 0

def handle_events():
    global rate, state, cursor_type
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == KEYDOWN:
            if event.key == 275:
                rate += 5
            elif event.key == 276:
                rate -= 5
                if rate <= 0:
                    rate = 0
            elif event.key == 27:
                exit()
            elif 49 <= event.key <= 52:
                cursor_type = (49,50,51,52).index(event.key)
            # Also show 0 FPS
            if rate <= 0:
                pygame.display.update(screen.blit(font.render("0   FPS", True,  ((0,0,0), pygame.Color("red"), pygame.Color("orange"), pygame.Color("yellow"))[cursor_type], (50, 195, 50)), (0,0)))


        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                state.cells.append(Cell(event.pos, DNA(wall_type=cursor_type)))
                # Draw the cell immediately
                body = (255-(cell.age*10),)*3
                pygame.draw.circle(screen, body, state.cells[-1].position, state.cells[-1].radius-3)
                border = (pygame.Color("black"), pygame.Color("red"), pygame.Color("orange"), pygame.Color("yellow"))[state.cells[-1].dna.wall_type]
                pygame.display.update(pygame.draw.circle(screen, border, state.cells[-1].position, state.cells[-1].radius, 4))
            elif event.button == 3:
                if cursor_type:
                    state.discs.append(Disc(event.pos, cursor_type))
                else:
                    state.discs.append(Disc(event.pos, randint(1,3)))
                # Draw the disk immediately
                color = (0, pygame.Color("red"), pygame.Color("orange"), pygame.Color("yellow"))[state.discs[-1].type]
                pygame.display.update(pygame.draw.circle(screen, color, state.discs[-1].position, state.discs[-1].radius))

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
        color = (0, pygame.Color("red"), pygame.Color("orange"), pygame.Color("yellow"))[disc.type]
        pygame.draw.circle(screen, color, disc.position, disc.radius)

    # Third, draw cells
    for cell in state.cells:
        body = (255-(cell.age*10),)*3
        pygame.draw.circle(screen, body, cell.position, cell.radius-3)
        border = (pygame.Color("black"), pygame.Color("red"), pygame.Color("orange"), pygame.Color("yellow"))[cell.dna.wall_type]
        pygame.draw.circle(screen, border, cell.position, cell.radius, 4)

    # Finally draw FPS indicator
    screen.blit(font.render("%s FPS" % int(round(clock.get_fps())), True,  ((0,0,0), pygame.Color("red"), pygame.Color("orange"), pygame.Color("yellow"))[cursor_type], (50, 195, 50)), (0,0))

    pygame.display.update()
    state.next()
