import pygame.draw
from pygame import Vector2
from pygame.draw import rect

from code.Const import C_PLAYER, ENTITY_SPEED, WIN_WIDTH, WIN_HEIGHT
from code.Entity import Entity

class Player(Entity):
    def __init__(self, mediator, name, x, y):
        super().__init__(mediator, name, x, y)
        self.type = 'player'
        self.x = x
        self.y = y
        self.position = Vector2(self.x, self.y)
        self.radius = 20

        self.health = 100
        self.speed = ENTITY_SPEED[self.name]

        # skills
        self.breathing = True
        self.breath_timer = 0
        self.breath_cooldown = 0
        self.facing_left = False

        self.walk_frames = []
        self.idle_frames = []
        frame_w = 55
        frame_h = 78

        sheet_idle = pygame.image.load(f'./assets/player_idle.png').convert_alpha()
        sheet_walk = pygame.image.load(f'./assets/player_walk.png').convert_alpha()

        # idle
        for i in range(4):
            frame = sheet_idle.subsurface((i * frame_w, 0, frame_w, frame_h))
            self.idle_frames.append(frame)

        # walk
        for i in range(4):
            frame = sheet_walk.subsurface((i*frame_w, 0, frame_w, frame_h))
            self.walk_frames.append(frame)

        self.state = 'idle'
        self.frame_index = 0
        self.animation_speed = 0.08

        self.image = self.idle_frames[0]
        self.rect = self.image.get_rect(center=(self.x, self.y))


    def draw(self, window):
        frames = self.walk_frames if self.state == 'walk' else self.idle_frames
        image = frames[int(self.frame_index)]

        if self.facing_left:
            image = pygame.transform.flip(image, True, False)

        window.blit(image, self.rect)

        if self.breathing:
            pygame.draw.circle(
                self.image,
                (150, 200, 255),
                (self.x, self.y),
                self.radius + 30,
                2
            )

    def update(self):
        pressed_key = pygame.key.get_pressed()

        moving = False

        if pressed_key[pygame.K_w]:
            self.position.y -= self.speed
            moving = True
        if pressed_key[pygame.K_a]:
            self.position.x -= self.speed
            moving = True
            self.facing_left = True
        if pressed_key[pygame.K_s]:
            self.position.y += self.speed
            moving = True
        if pressed_key[pygame.K_d]:
            self.position.x += self.speed
            moving = True
            self.facing_left = False

        if moving:
            self.state = 'walk'
        else:
            self.state = 'idle'

        self.frame_index += self.animation_speed

        frames = self.walk_frames if self.state == 'walk' else self.idle_frames

        if self.frame_index >= len(frames):
            self.frame_index = 0

        self.rect.center = self.position

        window_rect = pygame.Rect(0,0, WIN_WIDTH, WIN_HEIGHT)
        self.rect.clamp_ip(window_rect)

        # sincroniza posição
        self.position = pygame.Vector2(self.rect.center)

    def activate_skills(self):
        pass