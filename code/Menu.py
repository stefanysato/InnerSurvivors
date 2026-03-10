import sys
import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, C_WHITE
from code.Level import Level


class Menu:
    def __init__(self, window):
        self.window = window

    def run(self):
        self.text_generator(30, "press [space] to start", C_WHITE, (WIN_WIDTH/2, WIN_HEIGHT/2))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    level = Level(self.window)
                    level.run()

        pygame.display.flip()

    def text_generator(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font = pygame.font.SysFont(name="Lucida Console", size=text_size)
        text_surf = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)