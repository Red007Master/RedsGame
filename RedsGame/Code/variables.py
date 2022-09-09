import pygame
from mainShip import *
from drawableObject import *
from isRun import *

WIDTH = 1500
HEIGHT = 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

FPS = 60

RUN = isRun()

Sprite_Asteroids = []
Sprite_Ship_Normal = []
Sprite_Ship_Explosion = []

Sprite_Projectile = pygame.transform.scale(pygame.image.load("./Assets/Images/Projectile/projectile.png"), (10, 34))

Background0 = pygame.transform.scale(pygame.image.load("./Assets/Images/Background/0.png"), (WIDTH, HEIGHT))
Background1 = pygame.transform.scale(pygame.image.load("./Assets/Images/Background/1.png"), (WIDTH, HEIGHT))

MainShip = mainShip()
Asteroids = []
Projectiles = []

pygame.mixer.init()
Embient_sound = pygame.mixer.Sound('./Assets/Sounds/spaceEmbient.wav')
Thruster_sound = pygame.mixer.Sound('./Assets/Sounds/thruster.wav')
Laser_sound = pygame.mixer.Sound('./Assets/Sounds/laser.wav')
Asteroid_Brake = pygame.mixer.Sound('./Assets/Sounds/asteroidBrake.wav')

pygame.font.init()

FONT = pygame.font.SysFont(pygame.font.get_default_font(), 30)