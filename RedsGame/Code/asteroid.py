import random
from threading import Thread
from drawableObject import *
from variables import *

class asteroid(drawableObject):
    tick_speed = 0
    tick_counter = 0
    rotation_direction = 0

    def __init__(self):
        pass

    def generate(self, mainShip):
        self.set(Sprite_Asteroids[random.randint(0, len(Sprite_Asteroids) - 1)], 0, 0, 110, 110, random.randint(0, 360))

        self.tick_speed = random.randint(20, 100)
        self.rotation_direction = random.randint(0, 2)

        while True:
            x = random.randint(0, WIDTH)
            y = random.randint(0, HEIGHT)
            if (x > mainShip.pygame_rect.x - 100 and x < mainShip.pygame_rect.x + 100 and y > mainShip.pygame_rect.y - 100 and y < mainShip.pygame_rect.y + 100):
                continue
            else:
                self.change_position(x, y)
                break


    def tick(self):
        self.tick_counter += 1
        if (self.tick_counter >= self.tick_speed):
            if(self.rotation > 360):
                self.rotation = 0
            elif(self.rotation < 0):
                self.rotation = 360

            if(self.rotation_direction == 0):
                self.rotation += 1

            if(self.rotation_direction == 1):
                self.rotation -= 1

            self.tick_counter = 0