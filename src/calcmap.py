class Calcmap:

    def __init__(self,x,y):
	self.grid = range(y)

	for z in range(len(self.grid)):
	    self.grid[z] = range(x)

	    for a in range(len(self.grid[z])):
		self.grid[z][a]=0

    def consume (self,x,y,appetite=0.1):
	self.grid[y][x] -= appetite

    def select (self,x,y):
	return self.grid[y][x]

    def regrow(self,speed=0.05):
	for y in range(len(self.grid)):
	    for x in range(len(self.grid[y])):
		self.grid[y][x] += speed

		if (self.grid[y][x] > 1):
		    self.grid[y][x] = 1