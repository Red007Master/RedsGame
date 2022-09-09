import pygame
from variables import *
from projectile import *
from asteroid import *

TARGET_FIRE_COOLDOWN = 30
fire_cooldwon = 0
score = 0

def draw_drawable_object(drawable_object):
    WIN.blit(drawable_object.get_rotated_sprite(), (drawable_object.pygame_rect.x, drawable_object.pygame_rect.y))

def draw_background():
    WIN.blit(Background1, (0, 0))

def draw_foreground():
    draw_drawable_object(MainShip)

    for i in range(len(Projectiles)):
        draw_drawable_object(Projectiles[i])

    for i in range(len(Asteroids)):
        draw_drawable_object(Asteroids[i])

def draw_text():
    text = FONT.render("Score: " + str(score), True, (255, 255, 255))
    WIN.blit(text, (WIDTH - text.get_width() - 10, 10))

def draw_full():
    draw_background()
    draw_foreground()
    draw_text()
    pygame.display.update()

def move_key_pressed():
    MainShip.change_sprite(Sprite_Ship_Normal[0])
    Thruster_sound.set_volume(0.5)

def move_key_dont_pressed():
    MainShip.change_sprite(Sprite_Ship_Normal[1])
    Thruster_sound.set_volume(0)

def fire():

    projectile_x = 0
    projectile_y = 0

    if (MainShip.rotation == 0):
        projectile_x = MainShip.pygame_rect.x + MainShip.pygame_rect.width / 2
        projectile_y = MainShip.pygame_rect.y
    elif (MainShip.rotation == 90):
        projectile_x = MainShip.pygame_rect.x
        projectile_y = MainShip.pygame_rect.y + MainShip.pygame_rect.height / 2
    elif (MainShip.rotation == 180):
        projectile_x = MainShip.pygame_rect.x + MainShip.pygame_rect.width / 2
        projectile_y = MainShip.pygame_rect.y + MainShip.pygame_rect.height
    elif (MainShip.rotation == 270):
        projectile_x = MainShip.pygame_rect.x + MainShip.pygame_rect.width
        projectile_y = MainShip.pygame_rect.y + MainShip.pygame_rect.height / 2
    elif (MainShip.rotation == 45):
        projectile_x = MainShip.pygame_rect.x + MainShip.pygame_rect.width / 2
        projectile_y = MainShip.pygame_rect.y + MainShip.pygame_rect.height / 2
    elif (MainShip.rotation == 135):
        projectile_x = MainShip.pygame_rect.x + MainShip.pygame_rect.width / 2
        projectile_y = MainShip.pygame_rect.y + MainShip.pygame_rect.height / 2
    elif (MainShip.rotation == 225):
        projectile_x = MainShip.pygame_rect.x + MainShip.pygame_rect.width / 2
        projectile_y = MainShip.pygame_rect.y + MainShip.pygame_rect.height / 2
    elif (MainShip.rotation == 315):
        projectile_x = MainShip.pygame_rect.x + MainShip.pygame_rect.width / 2
        projectile_y = MainShip.pygame_rect.y + MainShip.pygame_rect.height / 2

    projectile = Projectile()
    projectile.set(Sprite_Projectile, projectile_x, projectile_y, 10, 34, MainShip.rotation)
    Projectiles.append(projectile)

    Laser_sound.play()

def check_keyboard_input():
    keys_pressed = pygame.key.get_pressed()
    
    if (keys_pressed[pygame.K_a]):
        MainShip.change_position(MainShip.pygame_rect.x - MainShip.speed, MainShip.pygame_rect.y)
        MainShip.change_rotation(90)
        move_key_pressed()

    if (keys_pressed[pygame.K_d]):
        MainShip.change_position(MainShip.pygame_rect.x + MainShip.speed, MainShip.pygame_rect.y)
        MainShip.change_rotation(270)
        move_key_pressed()

    if (keys_pressed[pygame.K_w]):
        MainShip.change_position(MainShip.pygame_rect.x, MainShip.pygame_rect.y - MainShip.speed)
        MainShip.change_rotation(0)
        move_key_pressed()

    if (keys_pressed[pygame.K_s]):
        MainShip.change_position(MainShip.pygame_rect.x, MainShip.pygame_rect.y + MainShip.speed)
        MainShip.change_rotation(180)
        move_key_pressed()

    if (keys_pressed[pygame.K_a] and keys_pressed[pygame.K_w]):
        MainShip.change_rotation(45)

    if (keys_pressed[pygame.K_a] and keys_pressed[pygame.K_s]):
        MainShip.change_rotation(135)

    if (keys_pressed[pygame.K_d] and keys_pressed[pygame.K_s]):
        MainShip.change_rotation(225)

    if (keys_pressed[pygame.K_d] and keys_pressed[pygame.K_w]):
        MainShip.change_rotation(315)

    if (not keys_pressed[pygame.K_a] and not keys_pressed[pygame.K_d] and not keys_pressed[pygame.K_w] and not keys_pressed[pygame.K_s]):
        move_key_dont_pressed()

    if (keys_pressed[pygame.K_ESCAPE]):
        RUN.set(False)

    if (keys_pressed[pygame.K_SPACE]):
        global fire_cooldwon

        if (fire_cooldwon == 0):
            fire_cooldwon = TARGET_FIRE_COOLDOWN
            fire()

    if (fire_cooldwon > 0):
        fire_cooldwon -= 1
            
def process_projectiles():
    for i in range(len(Projectiles)):
        Projectiles[i].tick()

        if (Projectiles[i].pygame_rect.x < 0 or Projectiles[i].pygame_rect.x > WIDTH or Projectiles[i].pygame_rect.y < 0 or Projectiles[i].pygame_rect.y > HEIGHT):
            Projectiles.pop(i)
            break

def process_asteroids():
    for i in range(len(Asteroids)):
        Asteroids[i].tick()

def process_collisions(asteroids, projectiles, main_ship):
    for i in range(len(asteroids)):
        for j in range(len(projectiles)):
            if (asteroids[i].pygame_rect.colliderect(projectiles[j].pygame_rect)):
                asteroids.pop(i)
                tempass = asteroid()
                tempass.generate(MainShip)
                Asteroids.append(tempass)
                Asteroid_Brake.play()
                projectiles.pop(j)
                global score
                score += 1
                break

        if (asteroids[i].pygame_rect.colliderect(main_ship.pygame_rect)):
            RUN.set(False)

def logic():
    check_keyboard_input()
    process_projectiles()
    process_asteroids()
    process_collisions(Asteroids, Projectiles, MainShip)
        
