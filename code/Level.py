import random as rd
import sys
import pygame

from code.Const import WIN_HEIGHT, WIN_WIDTH, EVENT_ENEMY, SPAWN_TIME, C_PLAYER, EVENT_TIMEOUT, TIMEOUT_STEP, \
    TIMEOUT_LEVEL
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator


class Level:
    def __init__(self, window):
        self.window = window
        self.mediator =  EntityMediator()
        self.factory = EntityFactory(self.mediator)

        self.factory.create_player('player', WIN_WIDTH/2, WIN_HEIGHT/2)

        self.time_count = TIMEOUT_STEP
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)

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
                if event.type == EVENT_TIMEOUT:
                    self.time_count += TIMEOUT_STEP
                    if self.time_count == TIMEOUT_LEVEL:
                        for ent in self.mediator.entities:
                            if ent.name == 'player':
                                # ent.score += ?
                                pass
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.mediator.player.breath.activate()



            for entity in self.mediator.entities:
                entity.update()
                entity.draw(self.window)
                if entity.name == 'player':
                    self.text_generator(14, f'Estabilidade: {entity.stability:.0f}', C_PLAYER, (10,10))
                    self.text_generator(14, f'Energia: {entity.stamina:.0f}', C_PLAYER, (10,30))
                    self.text_generator(14, f'Velocidade: {entity.speed}', C_PLAYER, (10,50))


            self.text_generator(14, f'Tempo decorrido: {self.time_count / 1000}', C_PLAYER, (WIN_WIDTH/2, 20))

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

    def text_generator(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font = pygame.font.SysFont(name="Lucida Console", size=text_size)
        text_surf = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)