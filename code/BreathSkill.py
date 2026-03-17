import pygame

from code.Const import C_BREATH, WIN_WIDTH
from code.Skill import Skill


class BreathSkill(Skill):
    def __init__(self, player):
        Skill.__init__(self, player)
        self.radius = 60
        self.duration = 3000  # 3s
        self.cooldown = 10000  # 10s
        self.end_time = -self.cooldown

    def draw(self, window):
        if not self.active:
            return

        pygame.draw.circle(window, C_BREATH, self.player.rect.center, self.radius, 3)