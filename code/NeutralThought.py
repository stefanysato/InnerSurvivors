import pygame.draw

from code.Entity import Entity


class NeutralThought(Entity):
    def __init__(self, name, mediator, x, y):
        super().__init__(mediator, name, x, y)
        self.type = 'thought'
        self.position = x, y
        self.status = 'active' # / collected

    def update(self):
        pass

    def draw(self, window):
        pygame.draw.circle(window, 'white', (self.x, self.y), 20, 0)
