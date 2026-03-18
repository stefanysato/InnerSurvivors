import math

import pygame.draw

from code.Entity import Entity


class NeutralThought(Entity):
    def __init__(self, name, mediator, x, y):
        super().__init__(mediator, name, x, y)
        self.type = 'thought'
        self.status = 'active' # / collected

        self.float_speed = 0.005
        self.float_amplitude = 5

        self.thought_surf = pygame.image.load('./assets/thought.png').convert_alpha()
        self.thought_rect = self.thought_surf.get_rect(center=(x, y))

    def update(self):
        now = pygame.time.get_ticks()
        offset = math.sin(now * self.float_speed) * self.float_amplitude

        self.thought_rect.y = self.y + offset

    def draw(self, window):
        window.blit(self.thought_surf, self.thought_rect)
