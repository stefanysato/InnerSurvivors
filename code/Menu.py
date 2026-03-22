import sys

import pygame
from code.Const import WIN_HEIGHT, C_WHITE, MENU_OPTION, C_BREATH, C_BG, WIN_WIDTH, F_JBMONO, F_AMATIC, F_ROBOTO


class Menu:
    def __init__(self, window):
        self.window = window
        self.bg = pygame.image.load('./assets/menu_bg.png').convert_alpha()
        self.bg_rect = self.bg.get_rect(left=550, top=30)

    def run(self):
        pygame.mixer.music.load('./assets/sounds/menu.wav')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

        menu_option = 0
        while True:
            self.window.fill(C_BG)
            self.window.blit(self.bg, self.bg_rect)
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.text(40, MENU_OPTION[i], F_AMATIC, C_BREATH, (50, WIN_HEIGHT - 250 + 50 * i))
                else:
                    self.text(40, MENU_OPTION[i], F_AMATIC, C_WHITE, (50, WIN_HEIGHT - 251 + 50 * i))

            # game title
            self.text(70, 'Inner', F_AMATIC, C_BREATH, text_pos=(90, 50))
            self.text(80, 'Survivors', F_AMATIC ,C_BREATH, text_pos=(50, 100))

            # controls
            self.text(30, 'CONTROLES', F_JBMONO, C_BREATH, text_pos=(WIN_WIDTH-30, WIN_HEIGHT-230), anchor="bottomright")

            keys1 = pygame.image.load('./assets/keys1.png').convert_alpha()
            self.window.blit(keys1, (WIN_WIDTH-250, WIN_HEIGHT-210))
            self.text(16, 'Movimentação', F_JBMONO, C_BREATH, text_pos=(WIN_WIDTH-40, WIN_HEIGHT-160), anchor="bottomright")

            keys2 = pygame.image.load('./assets/keys2.png').convert_alpha()
            self.window.blit(keys2, (WIN_WIDTH - 250, WIN_HEIGHT - 170))
            self.text(16, 'Respiração', F_JBMONO, C_BREATH, text_pos=(WIN_WIDTH - 40, WIN_HEIGHT - 115),
                      anchor="bottomright")

            keys3 = pygame.image.load('./assets/keys3.png').convert_alpha()
            self.window.blit(keys3, (WIN_WIDTH - 250, WIN_HEIGHT - 120))
            self.text(14, 'Reestruturação', F_JBMONO, C_BREATH, text_pos=(WIN_WIDTH - 40, WIN_HEIGHT - 80),
                      anchor="bottomright")
            self.text(14, 'Cognitiva', F_JBMONO, C_BREATH, text_pos=(WIN_WIDTH - 40, WIN_HEIGHT - 60),
                      anchor="bottomright")


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

    def text(self, text_size: int, text: str, text_font:str, text_color: tuple, text_pos: tuple, anchor: str = "topleft"):
        text_font = pygame.font.Font(text_font, size=text_size)
        text_surf = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect()
        setattr(text_rect, anchor, text_pos)
        self.window.blit(source=text_surf, dest=text_rect)
