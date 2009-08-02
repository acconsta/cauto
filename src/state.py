#!/usr/bin/env python
import math
import random

from cell import Cell

class State:

	def __init__(self, AGE=10, dimensions=(200, 200)):
		self.AGE = AGE
		self.dimensions = dimensions
		self.cells = []
		self.time = 0
		# Start off with a cell in each corner
		self.cells.append(Cell((11, 11)))
		self.cells.append(Cell((11, dimensions[1]-11)))
		self.cells.append(Cell((dimensions[0]-11, 11)))
		self.cells.append(Cell((dimensions[0]-11, dimensions[1]-11)))

	def next(self, speed=1):
		# Cells older than AGE reproduce
		for x in range(len(self.cells)):
			try:
				if self.cells[x].age == self.AGE:
					if self.cells[x].health >= 50:
						# First daughter, tangent to current
						newCell = Cell(self.cells[x].position, self.cells[x].dna.mutate())
						for theta in range(0, 200 * math.pi, 200 * math.pi / 18):
							newCell.position = (self.cells[x].position[0] + self.cells[x].radius * math.cos(theta / 100), \
												self.cells[x].position[1] + self.cells[x].radius * math.sin(theta / 100))
							if not self.checkCollision(newCell, self.cells[x]):
								self.cells.append(newCell)
								break
						# Second daughter, in same place as current
						self.cells.append(Cell(self.cells[x].position, self.cells[x].dna.mutate()))
						# Kill current cell
						self.cells[x].health = 0
					else:
						self.cells[x].health = 0
				else:
					self.cells[x].age += 1
			except:
				pass

		# Remove dead cells
		for y in range(len(self.cells)):
			try:
				if (self.cells[y].health <= 0):
					self.cells.pop(y)
				else:
					pass
			except:
				pass
		
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

	def checkCollision(self, cell1):
		# Check boundary collisions
		if (cell1.position[0]-cell1.radius < 0) or (cell1.position[0] + cell1.radius > self.dimensions[0]) \
		or (cell1.position[1]-cell1.radius < 0) or (cell1.position[1] + cell1.radius > self.dimensions[1]):
			return True
		# Check cell collisions
		for x in xrange(self.cells):
			if self.distanceSquared(self.cells[x], cell1) < (cell1.radius ** 2 + self.cells[x].radius ** 2):
				return True
			return False

	def distanceSquared(self, cell1, cell2):
		'''Returns the distance between two cells'''
		dist = (cell1.position[0] - cell2.position[0]) ** 2 + (cell1.position[1] - cell2.position[1]) ** 2
		if dist > 1:
			return dist
		else:
			return 1