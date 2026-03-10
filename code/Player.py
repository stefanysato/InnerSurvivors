import pygame.draw

from code.Const import C_PLAYER
from code.Entity import Entity

class Player(Entity):
    def __init__(self, mediator, name, pos: tuple):
        super().__init__(mediator, name, pos)
        self.type = 'player'
        self.pos = pos
        self.radius = 20
        # self.surf = pygame.image.load('./assets/player.png')

        self.health = 100

        # skills
        self.breathing = False
        self.breath_timer = 0
        self.breath_cooldown = 0



    def draw(self, window):
        pygame.draw.circle(window, C_PLAYER, center=self.pos, radius=self.radius)

        if self.breathing:
            pygame.draw.circle(
                window,
                (150, 200, 255),
                self.pos,
                self.radius + 30,
                2
            )

    def update(self):
        pressed_key = pygame.key.get_pressed()

        if pressed_key[pygame.K_w]:
            pass
        if pressed_key[pygame.K_a]:
            pass
        if pressed_key[pygame.K_s]:
            pass
        if pressed_key[pygame.K_d]:
            pass

    def activate_skills(self):
        pass