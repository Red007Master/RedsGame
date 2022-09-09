from drawableObject import *
from variables import *
import math

class Projectile(drawableObject):
    speed = 20

    def __init__(self):
        pass

    def tick(self):
        self.pygame_rect.x -= self.speed * math.sin(math.radians(self.rotation))
        self.pygame_rect.y -= self.speed * math.cos(math.radians(self.rotation))



