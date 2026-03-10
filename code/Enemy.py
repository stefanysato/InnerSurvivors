import random
import pygame
from pygame import Vector2

from code.Const import C_ANXIETY, C_PROC, ENTITY_SPEED, WIN_CENTER
from code.Entity import Entity

class Enemy(Entity):
    def __init__(self, mediator, name, pos: tuple):
        super().__init__(mediator, name, pos)
        self.pos = pos
        self.type = 'enemy'

    def draw(self, window):
        match self.name:
            case 'anxiety':
                shake_x = random.randint(-2, 2)
                shake_y = random.randint(-2, 2)

                pygame.draw.circle(
                    window,
                    C_ANXIETY,
                    (int(self.pos[0] + shake_x), int(self.pos[1] + shake_y)),
                    10
                )

            case 'procrastination':
                pygame.draw.circle(window, C_PROC, self.pos, 20)

            case 'guilt':
                pass

    def update(self):
        # move em direção ao centro (TESTE)
        direction = Vector2(WIN_CENTER) - self.pos
        if direction.length() > 0:
            direction = direction.normalize()
        self.pos += direction * ENTITY_SPEED[self.name]