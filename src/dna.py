from random import *
"""DNA Class

Stores the following attributes:
    -Wall width
    -Wall type
    -Toxin strength
    -Toxin type

mutate() returns a new dna object close (but a little different) from the current dna

GPL v.3 or later"""

class DNA:

    def __init__(self, wall_width=-1, wall_type=-1, toxin_strength=-1, toxin_type=-1):

        if (wall_width == -1):
            self.wall_width = random()
        else:
            self.wall_width = wall_width

        if (wall_type == -1):
            self.wall_type = randint (0, 3)
        else:
            self.wall_type = wall_type

        if (toxin_strength == -1):
            self.toxin_strength = 10 * random()
        else:
            self.toxin_strength = toxin_strength

        if (toxin_type == -1):
            self.toxin_type = randint(0, 3)
        else:
            self.toxin_type = toxin_type

    def __str__(self):
        return \
        """Wall width: %s
Wall type: %s
Toxin strength: %s
Toxin type: %s""" % (self.wall_width, self.wall_type, self.toxin_strength, self.toxin_type)

    def mutate(self):

        new_wall_width = self.wall_width + random() / 10

        if (new_wall_width < 0):
            new_wall_width = 0

        if (new_wall_width > 1):
            new_wall_width = 1

        if (random() > 0.9):
            new_wall_type = randint(0, 3)
        else:
            new_wall_type = self.wall_type

        new_toxin_strength = self.toxin_strength + random() / 10

        if (new_toxin_strength < 0):
            new_toxin_strength = 0

        if (new_toxin_strength > 1):
            new_toxin_strengh = 1

        if (random() > 0.9):
            new_toxin_type = randint(0, 3)
        else:
            new_toxin_type = self.toxin_type

        new_dna = DNA(new_wall_width, new_wall_type, new_toxin_strength, new_toxin_type)

        return new_dna
