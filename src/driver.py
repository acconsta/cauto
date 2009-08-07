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

state = State(dimensions=(600,600))
pygame.init()
screen = pygame.display.set_mode(state.dimensions, pygame.FULLSCREEN)
pygame.display.set_caption("Cauto: Extended Cellular Automata")

clock = pygame.time.Clock()
rate = 10 # Initial rate
oldrate = 0

cursor_type = 0

def handle_events():
    global rate, state, cursor_type, oldrate
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
            elif event.key == 32:
                if oldrate:
                    rate, oldrate = oldrate, 0
                else:
                    oldrate, rate = rate, 0
            elif event.key == 27:
                exit()
            elif 49 <= event.key <= 52:
                cursor_type = (49,50,51,52).index(event.key)
            # Also show 0 FPS
            if rate <= 0:
                pygame.display.update(screen.blit(font.render("0   FPS", True, ((0,0,0), \
pygame.Color("red"), pygame.Color("orange"), pygame.Color("yellow"))[cursor_type], (255, 255, 255)), (0,0)))
        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                state.cells.append(Cell(event.pos, DNA(wall_type=cursor_type)))
                # Draw the cell immediately
                body = (255-(state.cells[-1].age*10),)*3
                pygame.draw.circle(screen, body, state.cells[-1].position, state.cells[-1].radius-3)
                border = (pygame.Color("black"), pygame.Color("red"), pygame.Color("orange"), pygame.Color("yellow"))[state.cells[-1].dna.wall_type]
                pygame.display.update(pygame.draw.circle(screen, border, state.cells[-1].position, state.cells[-1].radius, 4))
            elif event.button == 3:
                if cursor_type:
                    state.discs.append(Disc(event.pos, cursor_type))
                else:
                    state.discs.append(Disc(event.pos, randint(1,3)))
                # Draw the disc immediately
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
    screen.fill((255, 255, 255))
    for a in xrange(len(state.themap.grid)):
        for b in xrange(len(state.themap.grid[a])):
            if state.themap.grid[b][a][0] != 1:
                screen.fill((155+state.themap.grid[b][a][0]*100,155+state.themap.grid[b][a][0]*100,155+state.themap.grid[b][a][0]*100), \
pygame.Rect(a*state.themap.cell_width,b*state.themap.cell_height,state.themap.cell_width,state.themap.cell_height))
    
    # Second, draw antibiotic discs
    for disc in state.discs:
        color = (0, pygame.Color("red"), pygame.Color("orange"), pygame.Color("yellow"))[disc.type]
        effect_area = pygame.Surface((200,200))
        effect_area.fill((255,255,255))
        effect_area.set_colorkey((255,255,255))
        pygame.draw.circle(effect_area, color, (100,100), 100)
        effect_area.set_alpha(75)
        screen.blit(effect_area, (disc.position[0]-100,disc.position[1]-100))
        pygame.draw.circle(screen, color, disc.position, disc.radius)
        
    # Third, draw cells
    for cell in state.cells:
        body_color = (255-(cell.age*10),)*3
        pygame.draw.circle(screen, body_color, cell.position, cell.radius-3)
        border_color = (pygame.Color("black"), pygame.Color("red"), pygame.Color("orange"), pygame.Color("yellow"))[cell.dna.wall_type]
        pygame.draw.circle(screen, border_color, cell.position, cell.radius, 4)
    
    # Finally draw FPS indicator
    screen.blit(font.render("%s FPS" % int(round(clock.get_fps())), True,  ((0,0,0), \
pygame.Color("red"), pygame.Color("orange"), pygame.Color("yellow"))[cursor_type], (255, 255, 255)), (0,0))

    pygame.display.update()
    state.next()
