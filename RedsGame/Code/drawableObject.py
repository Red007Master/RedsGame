import pygame

class drawableObject:
    pygame_rect = None
    sprite = None
    rotation = 0

    def __init__(self):
        pass

    def get_rotated_sprite(self):
        return pygame.transform.rotate(self.sprite, self.rotation)

    def set(self, sprite, x, y, width, height, rotation = 0):
        self.sprite = sprite
        self.pygame_rect = pygame.Rect(x, y, width, height)
        self.rotation = rotation

    def change_rotation(self, rotation):
        self.rotation = rotation

    def change_sprite(self, sprite):
        self.sprite = sprite

    def change_position(self, x, y):
        self.pygame_rect.x = x
        self.pygame_rect.y = y
