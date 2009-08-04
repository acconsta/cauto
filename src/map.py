#/usr/bin/python

class Map:

    def __init__(self,x,y):
	self.grid = range(y)
	for z in range(len(self.grid)):
	    self.grid[z]=range(x)
	    for a in range(len(self.grid[z])):
		self.grid[z][a] = 0
