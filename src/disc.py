import random

class Disc:
    def __init__(self, position=(0,0), type = -1, radius = 15):
        # Default attributes
        self.position = position
        self.age = random.randint(0,5)
        self.radius = radius
        
        # DNA
        if (type == -1):
            self.type = random.randint(1, 3)
        else:
            self.type = type
                
    def __str__(self):
        return \
        """position %s
        age %s
        type %s""" % (self.position, self.age, self.type)