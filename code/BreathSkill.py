import pygame

from code.Const import C_BREATH
from code.Skill import Skill

class BreathSkill(Skill):
    def __init__(self, player):
        Skill.__init__(self, player)
        self.radius = 60

    def draw(self, window):
        if not self.active:
            return

        pygame.draw.circle(window, C_BREATH, self.player.rect.center, self.radius, 4)