#!/usr/bin/env python
import math

from cell import Cell
from calcmap import Calcmap
from random import *

class State:

    def __init__(self, AGE=10, dimensions=(200, 200)):
        self.AGE = AGE
        self.dimensions = dimensions
        self.cells = []
        self.time = 0
        # Start off with a cell in the center
        self.cells.append(Cell((dimensions[0]/2, dimensions[1]/2)))
	#Initiate map with full nutrients
	self.themap = Calcmap(dimensions[0],dimensions[1],20,20)


    def next(self, speed=1):
	print (len(self.cells))
	print self.themap.grid
        # Cells older than AGE reproduce
        for cell in self.cells:
	    print ('next cell')
            if cell.age >= self.AGE:
		print ('next mature cell')
                if cell.health >= 50:
		    print ("Binary fission time!")
                    # Add two tangent daughter cells
                    newCell = Cell(cell.position, cell.dna.mutate())
                    theta = uniform(0, 200 * math.pi)
                    newCell.position = (cell.position[0] + cell.radius * 2 * math.cos(theta / 100), \
		      cell.position[1] + cell.radius * 2 * math.sin(theta / 100))
                    self.cells.append(newCell)
		    # Second daughter, in same place as current
                    self.cells.append(Cell(cell.position, cell.dna.mutate()))
                # Kill current cell
                    cell.health = 0
                else:
                    cell.health = 0
            else:
		break

	for z in self.cells:
	    z.age += speed
	    z.health *= self.themap.select(z.position[0],z.position[1])
	    if (z.health > 100):
		z.health = 100
	    elif (z.health < 0):
		z.health = 0
	    self.themap.consume(z.position[0],z.position[1])

        # Remove dead cells
        for y in range(len(self.cells)):
            try:
                if (self.cells[y].health <= 0):
                    self.cells.pop(y)
            except IndexError:
                pass

	self.themap.regrow()
        self.time += 1

    def __str__(self):
        return_str = "Cells:"

        for x in self.cells:
            return_str += "\n---\n"
            return_str += str(x)

        return return_str

    def add_cell(self, cell=Cell((0, 0))):
        self.cells.append(cell)

    def pop_first_cell(self):
        return self.cells.pop()

    def check_collision(self, x, y, radius):
	print ('Collision check')
        # Check boundary collisions
        if (x-radius < 0) or (x + radius > self.dimensions[0]) \
        or (y-radius < 0) or (y + radius > self.dimensions[1]):
            return True
        # Check cell collisions
        for cell2 in self.cells:
            if self.distance_squared(cell2.position[0], cell2.position[1], x, y) < (radius + cell2.radius) ** 2:
                return True
            return False

    def distance_squared(self, x, y, x2, y2):
        '''Returns the distance between two cells'''
        dist = (x - x2) ** 2 + (y - y2) ** 2
        if dist > 1:
            return dist
        else:
            return 1