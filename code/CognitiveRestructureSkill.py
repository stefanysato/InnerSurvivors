import pygame

from code.Const import C_COGNIT
from code.Skill import Skill

class CognitiveRestructureSkill(Skill):
    def __init__(self, player):
        Skill.__init__(self, player)
        self.radius = 60
        self.duration = 2000
        self.cooldown = 10000
        self.end_time = -self.cooldown

    def draw(self, window):
        if not self.active:
            return

        pygame.draw.circle(window, C_COGNIT, self.player.rect.center, self.radius, 3)

