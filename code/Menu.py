import sys

import pygame
from code.Const import WIN_HEIGHT, C_WHITE, MENU_OPTION, C_BREATH, C_BG


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/menu_bg.png').convert_alpha()
        self.rect = self.surf.get_rect()

    def run(self):
        pygame.mixer.music.load('./assets/sounds/menu.wav')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

        menu_option = 0
        while True:
            self.window.blit(self.surf, self.rect)
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.text(40, MENU_OPTION[i], C_BREATH, (50, WIN_HEIGHT - 250 + 50 * i))
                else:
                    self.text(40, MENU_OPTION[i], C_WHITE, (50, WIN_HEIGHT - 251 + 50 * i))

            self.text(70, 'Inner', C_BREATH, text_pos=(90, 60))
            self.text(80, 'Survivors', C_BREATH, text_pos=(50, 100))


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    pygame.mixer.Sound('./assets/sounds/menu_select.wav').play()
                    if event.key == pygame.K_DOWN:
                        menu_option = (menu_option + 1) % len(MENU_OPTION) # loop circular com módulo
                    if event.key == pygame.K_UP:
                        menu_option = (menu_option - 1) % len(MENU_OPTION)
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]

            pygame.display.flip()

    def text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font = pygame.font.SysFont(name="./assets/fonts/AmaticSC.ttf", size=text_size)
        text_surf = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(topleft=text_pos)
        self.window.blit(source=text_surf, dest=text_rect)
