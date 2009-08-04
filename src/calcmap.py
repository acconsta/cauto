class Calcmap:

    def __init__(self,x,y,cell_width,cell_height):
	self.grid = range(int(y/cell_height))
	self.width = x
	self.height = y
	self.cell_width = cell_width
	self.cell_height = cell_height
	for z in range(len(self.grid)):
	    self.grid[z] = range(int(x/cell_width))

	    for a in range(len(self.grid[z])):
		self.grid[z][a]=0

    def consume (self,x,y,appetite=0.1):
	self.grid[int(y/self.cell_height)][int(x/self.cell_width)] -= appetite

    def select (self,x,y):
	return self.grid[int(y/self.cell_height)][int(x/self.cell_width)]

    def regrow(self,speed=0.05):
	for y in range(len(self.grid)):
	    for x in range(len(self.grid[y])):
		self.grid[y][x] += speed

		if (self.grid[y][x] > 1):
		    self.grid[y][x] = 1