import pygame

class Skill:
    def __init__(self, player):
        self.player = player
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

        # self.player.stamina -= self.player.stamina_drain

    def update(self):
        if not self.active:
            return

        now = pygame.time.get_ticks()

        if now - self.start_time > self.duration:
            self.active = False
            self.end_time = now

        # if self.active:
        #     if self.player.stamina <= 0:
        #         self.active = False
        #         self.player.stamina = 0
        # else:
        #     self.player.stamina += self.player.stamina_regen
        #     if self.player.stamina > self.player.max_stamina:
        #         self.player.stamina = self.player.max_stamina

    def draw(self, window):
        pass

