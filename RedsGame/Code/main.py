import pygame
from drawableObject import *
from variables import *
from initialization import *
from work import *

def one_cycle():
    logic()
    draw_full()

def main():
    initialize()

    WIN.blit(Background0, (0, 0))
    pygame.display.update()
    pygame.time.delay(1000)

    clock = pygame.time.Clock()

    global RUN
    while RUN.get():
        clock.tick(FPS)
 
        keys_pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                RUN.set(False)

        one_cycle()

    for i in range(len(Sprite_Ship_Explosion)):
        clock.tick(5)
        MainShip.change_sprite(Sprite_Ship_Explosion[i])
        draw_background()
        draw_drawable_object(MainShip)
        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()