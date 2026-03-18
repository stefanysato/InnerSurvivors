import random

import pygame
from pygame import Vector2

from code.Const import ENTITY_SPEED
from code.Entity import Entity
from code.NeutralThought import NeutralThought


class Enemy(Entity):
    def __init__(self, mediator, name, x, y):
        super().__init__(mediator, name, x, y)
        self.x = x
        self.y = y
        self.type = 'enemy'

        self.effect_applied = False
        self.status = {
            "repel": False,
            "transform": False
        }

        self.position = Vector2(self.x, self.y)

        self.knockback = pygame.Vector2(0, 0)
        self.knockback_force = 10
        self.knockback_decay = 0.85

        self.frames = []

        # anxiety
        if self.name == 'anxiety':
            sheet = pygame.image.load(f'./assets/{self.name}.png')
            frame_w = 50
            frame_h = 50

            self.frames = []

            for i in range(10):
                frame = sheet.subsurface((i * frame_w, 0, frame_w, frame_h))
                self.frames.append(frame)

        if self.name == 'procrastination':
            sheet = pygame.image.load(f'./assets/{self.name}.png')
            frame_w = 42
            frame_h = 37

            self.frames = []

            for i in range(4):
                frame = sheet.subsurface((i * frame_w, 0, frame_w, frame_h))
                self.frames.append(frame)

        if len(self.frames) > 0:
            self.image = self.frames[0]

        self.frame_index = 0
        self.animation_speed = 0.08
        self.rect = self.image.get_rect(center=self.position)

    def draw(self, window):
        match self.name:
            case 'anxiety':
                image = self.frames[int(self.frame_index)]
                shake_x = random.randint(-2, 2)
                shake_y = random.randint(-2, 2)

                draw_rect = self.rect.move(shake_x, shake_y)
                window.blit(image, draw_rect)

            case 'procrastination':
                image = self.frames[int(self.frame_index)]
                window.blit(image, self.rect)

    def update(self):
        player = self.mediator.get_player()

        direction = player.position - self.position
        if direction.length() > 0:
            direction = direction.normalize()

        # movimento normal
        self.position += direction * ENTITY_SPEED[self.name]

        # efeito das skills no inimigo
        # breath:
        if self.status['repel']:
            # direção oposta ao player
            direction = self.position - player.position

            if direction.length() > 0:
                direction = direction.normalize()
            self.knockback = direction * self.knockback_force
        # aplica knockback
        self.position += self.knockback
        # reduz knockback gradualmente
        self.knockback *= self.knockback_decay

        # transform
        if self.status["transform"]:
            self.mediator.remove(self)
            thought = NeutralThought("thought", self.mediator, self.position.x, self.position.y)
            self.mediator.register(thought)

        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.frame_index = 0

        if self.rect.colliderect(player.rect):
            if self.name == 'anxiety':
                player.stability -= 0.1
            if self.name == 'procrastination' and not self.effect_applied:
                player.speed = max(0.2, player.speed - 0.05)
                self.effect_applied = True

        self.rect.center = self.position
