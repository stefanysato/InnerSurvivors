import pygame

class Spritesheet:
    def __init__(self, name):
        self.name = name
        self.sheet = pygame.image.load(f'./assets/{self.name}.png').convert_alpha()


    def get_image(self, x,y, width, height):
        image = pygame.Surface((width, height), pygame.SRCALPHA)

        image.blit(
            self.sheet,
            (0,0),
            (x, y, width, height)
        )

        return image