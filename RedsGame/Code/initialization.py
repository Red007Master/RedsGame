import pygame
import os
from pygame.locals import *
from drawableObject import *
from variables import *
from asteroid import *

def load_spritesheet(spritesheets, frame, width, height, scale, colour):
		image = pygame.Surface((width, height))
		image.blit(spritesheets, (0, 0), ((frame * width), 0, width, height))
		image = pygame.transform.scale(image, (width * scale, height * scale))
		image.set_colorkey(colour)
		return image

def initialize():
    pygame.display.set_caption("Red'sSpaceGame")

    asteroid_files = os.listdir("./Assets/Images/Asteroids")

    for i in range(len(asteroid_files)):
        asteroid_spritesheets = pygame.image.load("./Assets/Images/Asteroids/" + asteroid_files[i])
        for j in range(8):
            Sprite_Asteroids.append(load_spritesheet(asteroid_spritesheets, i, 100, 100, 1, (0, 0, 0)))

    ship_files_normal = os.listdir("./Assets/Images/Ship/Normal")
    ship_files_explosion = os.listdir("./Assets/Images/Ship/Explosion")

    for i in range(len(ship_files_normal)):
        Sprite_Ship_Normal.append(pygame.transform.rotate(pygame.image.load("./Assets/Images/Ship/Normal/" + ship_files_normal[i]).convert_alpha(), 90))

    for i in range(len(ship_files_explosion)):
        Sprite_Ship_Explosion.append(pygame.transform.rotate(pygame.image.load("./Assets/Images/Ship/Explosion/" + ship_files_explosion[i]).convert_alpha(), 90))

    global Background
    Background = pygame.image.load("./Assets/Images/Background/1.png").convert_alpha()

    global MainShip
    MainShip.set(Sprite_Ship_Normal[1], WIDTH / 2 - 50, HEIGHT / 2 - 50, 60, 60)

    global Explosion_Sound
    Embient_sound.play()
    Embient_sound.set_volume(0.05)

    global Thruster_sound
    Thruster_sound.set_volume(0)
    Thruster_sound.play(-1, 0)

    global Laser_sound
    Laser_sound.set_volume(0.1)

    global Asteroid_Brake
    Asteroid_Brake.set_volume(0.03)

    for i in range(10):
        tempass = asteroid()
        tempass.generate(MainShip)
        Asteroids.append(tempass)

    global Run
    Run = 1

    




