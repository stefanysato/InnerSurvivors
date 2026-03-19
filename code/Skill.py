import pygame

class Skill:
    def __init__(self, player, mediator):
        self.player = player
        self.mediator = mediator
        self.active = False

        self.start_time = 0
        self.end_time = 0

        self.duration = 0
        self.cooldown = 0

    def can_activate(self):
        now = pygame.time.get_ticks()
        return now - self.end_time >= self.cooldown

    def activate(self):
        if self.active:
            return

        if not self.can_activate():
            return

        self.active = True
        self.start_time = pygame.time.get_ticks()

    def update(self):
        if not self.active:
            return

        now = pygame.time.get_ticks()

        if now - self.start_time > self.duration:
            self.active = False
            self.end_time = now

    def get_cooldown_progress(self):
        now = pygame.time.get_ticks()
        elapsed = now - self.end_time

        if self.cooldown == 0:
            return 1
        return min(1, elapsed / self.cooldown)

    def draw(self, window):
        pass
