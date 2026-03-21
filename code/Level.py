import random as rd
import sys

import pygame

from code.Const import WIN_HEIGHT, WIN_WIDTH, EVENT_ENEMY, SPAWN_TIME, TIME_VICTORY, C_BG, SPAWN_INTERVAL, \
    C_WHITE
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.HUD import HUD


class Level:
    def __init__(self, window):
        self.window = window
        self.mediator = EntityMediator()
        self.factory = EntityFactory(self.mediator)

        self.player = self.factory.create_player('player', WIN_WIDTH / 2, WIN_HEIGHT / 2)
        self.player.score = 0

        self.neutral_thoughts = self.mediator.thoughts

        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        self.spawn_time = SPAWN_TIME
        self.last_difficulty_increase = pygame.time.get_ticks()

        self.start_time = pygame.time.get_ticks()

        self.victory_achieved = False
        self.victory_time_reached = 0

        self.hud = HUD(self.player, window)

    def run(self):
        pygame.mixer.music.stop()
        while True:
            self.window.fill(C_BG)
            clock = pygame.time.Clock()
            clock.tick(60)

            now = pygame.time.get_ticks()
            elapsed = now - self.start_time

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = rd.choice(('anxiety', 'procrastination'))
                    self.factory.create_enemy(choice, self.spawn_enemy()[0], self.spawn_enemy()[1])
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.mediator.player.skills[0].activate()
                    if event.key == pygame.K_LSHIFT:
                        self.mediator.player.skills[1].activate()
                    if event.key == pygame.K_ESCAPE:
                        return

            if now - self.last_difficulty_increase >= SPAWN_INTERVAL:
                self.last_difficulty_increase = now
                self.spawn_time = max(500, int(self.spawn_time * 0.9))
                pygame.time.set_timer(EVENT_ENEMY, self.spawn_time)
                print(self.spawn_time)

            # se passar do tempo, considera vitória
            if not self.victory_achieved and elapsed > TIME_VICTORY:
                self.victory_achieved = True

            if self.player.is_dead:
                score = self.calculate_score()
                return score, self.victory_achieved, elapsed


            for entity in self.mediator.entities:
                entity.update()
                entity.draw(self.window)

            for thought in self.neutral_thoughts:
                if self.player.rect.colliderect(thought.rect):
                    thought.collected = True
                    thought.collect_time = pygame.time.get_ticks()
                    self.player.collect_thought(thought)
                    self.neutral_thoughts.remove(thought)

            self.player.is_slowed = False

            for enemy in self.mediator.enemies:
                if enemy.rect.colliderect(self.player.rect):
                    if enemy.name == 'procrastination':
                        self.player.is_slowed = True

            self.text(14, f'Tempo decorrido: {(elapsed/1000):.0f}s', C_WHITE, (WIN_WIDTH - 10, 10))
            self.text(14, f'Pensamentos Neutros: {self.player.thoughts_collected}', C_WHITE, (WIN_WIDTH - 10, 30))

            self.hud.draw(self.window)
            pygame.display.flip()

    def calculate_score(self):
        total_time = pygame.time.get_ticks() - self.start_time
        time_seconds = total_time // 1000

        bonus = 0
        if self.victory_achieved:
            extra_time = (total_time - TIME_VICTORY) // 1000
            bonus = max(0, extra_time * 2)

        score = (
                self.player.thoughts_collected * 10
                + time_seconds
                + bonus
        )

        return score

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
        return x, y

    def text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font = pygame.font.SysFont(name="Verdana", size=text_size)
        text_surf = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(topright=text_pos)
        self.window.blit(source=text_surf, dest=text_rect)
