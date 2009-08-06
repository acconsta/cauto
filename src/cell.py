import random
from dna import DNA

class Cell:
    def __init__(self, position=(0,0), dna=-1, radius = 10):
        # Default attributes
        self.position = position
        self.age = random.randint(0,5)
        self.health = 100
        self.radius = radius

        # DNA
        if (dna == -1):
            self.dna = DNA()
        else:
            self.dna = dna

    def reproduce(self):
        return Cell((0,0), dna.mutate())

    def __str__(self):
        return \
"""position %s
age %s
health %s
dna.wall_width %s
dna.wall_type %s
dna.toxin_strength %s
dna.toxin_type %s""" % (self.position, self.age, self.health, self.dna.wall_width, self.dna.wall_type, \
                        self.dna.toxin_strength, self.dna.toxin_type)

##testCell = Cell((0,0))
##print testCell