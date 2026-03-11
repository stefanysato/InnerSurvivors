import random
import pygame
from pygame import Vector2

from code.Const import ENTITY_SPEED
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, mediator, name, x, y):
        super().__init__(mediator, name, x, y)
        self.x = x
        self.y = y
        self.type = 'enemy'

        self.position = Vector2(self.x, self.y)

        self.frames = []

        # anxiety
        if self.name == 'anxiety':
            sheet = pygame.image.load(f'./assets/{self.name}.png')
            frame_w = 33
            frame_h = 61

            self.frames = []

            for i in range(6):
                frame = sheet.subsurface((i*frame_w, 0, frame_w, frame_h))
                self.frames.append(frame)

        if self.name == 'procrastination':
            sheet = pygame.image.load(f'./assets/{self.name}.png')
            frame_w = 58
            frame_h = 30

            self.frames = []

            for i in range(6):
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

            case 'guilt':
                pass

    def update(self):
        player = self.mediator.get_player()

        direction = player.position - self.position
        if direction.length() > 0:
            direction = direction.normalize()
        self.position += direction * ENTITY_SPEED[self.name]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.frame_index = 0

        self.rect.center = self.position