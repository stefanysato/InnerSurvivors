import pygame

from code.Const import C_BREATH, WIN_WIDTH
from code.Skill import Skill


class BreathControl(Skill):
    def __init__(self, player, mediator):
        Skill.__init__(self, player, mediator)
        self.radius = 60
        self.duration = 3000  # 3s
        self.cooldown = 15000  # 10s
        self.end_time = -self.cooldown

    def update(self):
        super().update()

        if not self.active:
            return

        self.mediator.push_enemies(self.player)

    def draw(self, window):
        if not self.active:
            return

        pygame.draw.circle(window, C_BREATH, self.player.rect.center, self.radius, 3)