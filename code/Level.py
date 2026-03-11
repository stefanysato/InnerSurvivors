import random as rd
import sys
import pygame

from code.Const import WIN_HEIGHT, WIN_WIDTH, EVENT_ENEMY, SPAWN_TIME
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator

class Level:
    def __init__(self, window):
        self.window = window
        self.mediator =  EntityMediator()
        self.factory = EntityFactory(self.mediator)

        self.factory.create_player('player', WIN_WIDTH/2, WIN_HEIGHT/2)

        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
    def run(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            self.window.fill('gray')

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = rd.choice(('anxiety', 'procrastination'))
                    self.factory.create_enemy(choice, self.spawn_enemy()[0], self.spawn_enemy()[1])

            for entity in self.mediator.entities:
                entity.update()
                entity.draw(self.window)

            pygame.display.flip()

    @staticmethod
    def spawn_enemy():
        side = rd.choice(('top', 'bottom', 'left', 'right'))
        if side == 'top':
            x = rd.randint(0, WIN_WIDTH)
            y = -50
        elif side == 'bottom':
            x = rd.randint(0, WIN_WIDTH)
            y = WIN_HEIGHT + 50
        elif side == 'left':
            x = -50
            y = rd.randint(0, WIN_HEIGHT)
        elif side == 'right':
            x = WIN_WIDTH + 50
            y = rd.randint(0, WIN_HEIGHT)
        return x,y