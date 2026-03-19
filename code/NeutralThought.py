import math
import pygame.draw

from code.Entity import Entity


class NeutralThought(Entity):
    def __init__(self, name, mediator, x, y):
        super().__init__(mediator, name, x, y)
        self.type = 'thought'
        self.value = 2

        self.collected = False
        self.collect_time = 0
        self.collect_duration = 500 # ms

        self.float_speed = 0.005
        self.float_amplitude = 5

        self.surf = pygame.image.load('./assets/thought.png').convert_alpha()
        self.rect = self.surf.get_rect(center=(x, y))

    def update(self):
        now = pygame.time.get_ticks()
        offset = math.sin(now * self.float_speed) * self.float_amplitude

        self.rect.y = self.y + offset

        if self.collected:
            now = pygame.time.get_ticks()
            elapsed = now - self.collect_time

            if elapsed >= self.collect_duration:
                self.mediator.remove(self)

    def draw(self, window):
        window.blit(self.surf, self.rect)
