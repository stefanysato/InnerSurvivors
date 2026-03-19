import pygame

from code.Const import C_COGNIT
from code.Skill import Skill

class CognitiveRestructureSkill(Skill):
    def __init__(self, player, mediator):
        Skill.__init__(self, player, mediator)
        self.radius = 60
        self.duration = 2000 # 2s
        self.cooldown = 20000 # 15s
        self.end_time = -self.cooldown

    def update(self):
        super().update()

        if not self.active:
            return

        self.mediator.transform_to_neutral(self.player)

    def draw(self, window):
        if not self.active:
            return

        pygame.draw.circle(window, C_COGNIT, self.player.rect.center, self.radius, 3)

