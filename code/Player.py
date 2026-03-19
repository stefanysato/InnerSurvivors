import math
import pygame.draw
from code.BreathSkill import BreathSkill
from code.CognitiveRestructureSkill import CognitiveRestructureSkill
from code.Const import ENTITY_SPEED, WIN_WIDTH, WIN_HEIGHT
from code.Entity import Entity

class Player(Entity):
    def __init__(self, mediator, name, x, y):
        super().__init__(mediator, name, x, y)
        self.type = 'player'
        self.x = x
        self.y = y
        self.position = pygame.Vector2(self.x, self.y)

        self.stability = 100
        self.thoughts_collected = 0
        self.score = 0

        self.base_speed = ENTITY_SPEED[self.name]
        self.current_speed = self.base_speed
        self.slow_factor = 1.0
        self.is_slowed = False

        # skills
        self.skills = [
            BreathSkill(self, mediator),
            CognitiveRestructureSkill(self, mediator)
        ]

        self.facing_left = False
        self.idle_image = pygame.image.load(f'./assets/player_idle.png').convert_alpha()
        self.walk_frames = []
        self.skill_frames = []

        frame_w = 55
        frame_h = 78

        sheet_walk = pygame.image.load(f'./assets/player_walk.png').convert_alpha()
        sheet_skill = pygame.image.load(f'./assets/player_skill.png').convert_alpha()

        # skill
        for i in range(4):
            frame = sheet_skill.subsurface((i * frame_w, 0, frame_w, frame_h))
            self.skill_frames.append(frame)

        # walk
        for i in range(4):
            frame = sheet_walk.subsurface((i*frame_w, 0, frame_w, frame_h))
            self.walk_frames.append(frame)

        self.state = 'idle'
        self.frame_index = 0
        self.animation_speed = 0.08

        self.image = self.idle_image
        self.rect = self.image.get_rect(center=self.position)


    def draw(self, window):
        if self.facing_left:
            self.image = pygame.transform.flip(self.image, True, False)

        window.blit(self.image, self.rect)

        # draw skills
        for skill in self.skills:
            skill.draw(window)

    def collect_thought(self, thought):
        self.thoughts_collected += 1
        self.stability += thought.value


    def update(self):
        pressed_key = pygame.key.get_pressed()

        moving = False
        direction = pygame.Vector2(0,0)

        if pressed_key[pygame.K_w]:
            self.position.y -= self.current_speed
            moving = True
        if pressed_key[pygame.K_a]:
            self.position.x -= self.current_speed
            moving = True
            self.facing_left = True
        if pressed_key[pygame.K_s]:
            self.position.y += self.current_speed
            moving = True
        if pressed_key[pygame.K_d]:
            self.position.x += self.current_speed
            moving = True
            self.facing_left = False

        if self.is_slowed:
            self.current_speed = self.base_speed * 0.5
        else:
            self.current_speed = self.base_speed

        self.position += direction * self.current_speed

        if moving:
            self.state = 'walk'
        elif self.skills[0].active or self.skills[1].active:
            self.state = 'skill'
        else:
            self.state = 'idle'

        if self.state == "walk":
            self.frame_index += self.animation_speed

            if self.frame_index >= len(self.walk_frames):
                self.frame_index = 0

            self.image = self.walk_frames[int(self.frame_index)]

        elif self.state == "skill":
            self.frame_index += self.animation_speed

            if self.frame_index >= len(self.skill_frames):
                self.frame_index = 0

            self.image = self.skill_frames[int(self.frame_index)]
        else:
            self.image = self.idle_image
            self.frame_index = 0

        self.rect.center = (round(self.position.x), round(self.position.y))

        window_rect = pygame.Rect(0, 0, WIN_WIDTH, WIN_HEIGHT)
        self.rect.clamp_ip(window_rect)

        # sincroniza posição
        self.position = pygame.Vector2(self.rect.center)

        for skill in self.skills:
            skill.update()