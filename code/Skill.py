import pygame

class Skill:
    def __init__(self, player):
        self.player = player
        self.active = False
        self.start_time = 0
        self.duration = 2000

    def activate(self):
        self.active = True
        self.start_time = pygame.time.get_ticks()

        # self.player.stamina -= self.player.stamina_drain

    def update(self):
        if not self.active:
            return

        now = pygame.time.get_ticks()

        if now - self.start_time > self.duration:
            self.active = False

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