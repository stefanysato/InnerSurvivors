import datetime
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import C_BG, WIN_WIDTH, WIN_HEIGHT, C_BG_WIN, C_BG_LOSE, C_BLACK, C_BLUE_GREY, C_WHITE
from code.DBProxy import DBProxy


class Score:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
        self.name = ''
        self.max_chars = 8
        self.selected = True


    def save(self, score, victory, elapsed_time):
        input_rect = pygame.Rect((WIN_WIDTH / 2 - 100, 220), (200,30))
        color = C_BLUE_GREY

        db_proxy = DBProxy('DBScore')
        while True:
            self.window.blit(self.surf, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect.collidepoint(event.pos):
                        self.selected = True
                    else:
                        self.selected = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
                    if self.selected:
                        if event.key == pygame.K_RETURN:
                            db_proxy.save({'name':self.name, 'score':score, 'time':get_formatted_time(elapsed_time),'date': get_formatted_date()})
                            self.show()
                            return
                        elif event.key == pygame.K_BACKSPACE:
                            self.name = self.name[:-1]
                        else:
                            if len(self.name) < self.max_chars:
                                self.name += event.unicode

            if not victory:
                self.surf.fill(C_BG_LOSE)
                self.text(30, 'A ansiedade venceu dessa vez...', C_BG, (WIN_WIDTH / 2, 50))
            else:
                self.surf.fill(C_BG_WIN)
                self.text(30, 'Você estabilizou sua mente. :)', C_BG, (WIN_WIDTH / 2, 50))
                # type name - label
                self.text(20, 'Digite seu nome:', C_BG, (WIN_WIDTH / 2, 200))
                # type name - input
                pygame.draw.rect(self.window, color, input_rect, 3)
                self.text(20, self.name, C_BLACK, (0,0), dest_rect=(input_rect.x + 5, input_rect.y + 3))
                self.text(20, '[enter]', color, (WIN_WIDTH / 2, 270))

            if self.selected:
                color = C_BLACK
            else:
                color = C_BLUE_GREY

            # score
            self.text(40, f'Pontuação: {score}', C_BG, (WIN_WIDTH / 2, 100))
            self.text(20, f'Pressione [esc] para voltar ao menu', C_BG, (WIN_WIDTH / 2, WIN_HEIGHT-50))

            pygame.display.flip()

    def show(self):
        self.surf.fill(C_BG)
        self.window.blit(self.surf, (0, 0))

        border_rect = pygame.Rect((20,20), (WIN_WIDTH-40, WIN_HEIGHT-40))
        pygame.draw.rect(self.window, C_BLUE_GREY, border_rect, 2)

        bg_surf = pygame.image.load('./assets/breath_bg.png').convert_alpha()
        bg_rect = bg_surf.get_rect(bottomright = (WIN_WIDTH-30, WIN_HEIGHT - 30))
        self.window.blit(bg_surf, bg_rect)

        # posição colunas
        col_name = 60
        col_score = 280
        col_time = 360
        col_date = 500
        y = 120
        line_height = 30

        # titulo
        self.text(30, 'SCORE', C_BLACK, (50, 30), anchor='topleft')

        # cabeçalho
        self.text(20, 'Nome', C_BLUE_GREY, (col_name, 90), anchor='topleft')
        self.text(20, 'Score', C_BLUE_GREY, (col_score, 90), anchor='topright')
        self.text(20, 'Tempo', C_BLUE_GREY, (col_time, 90), anchor='topleft')
        self.text(20, 'Data', C_BLUE_GREY, (col_date, 90), anchor='topleft')

        # retrieve db
        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.show_results()
        db_proxy.close()

        for player_score in list_score:
            id_, name, score, elapsed_time, date = player_score
            self.text(20, str(name), C_WHITE, (col_name, y), anchor="topleft")
            self.text(20, str(score), C_WHITE, (col_score, y), anchor="topright")
            self.text(20, str(elapsed_time), C_WHITE, (col_time, y), anchor="topleft")
            self.text(20, str(date), C_WHITE, (col_date, y), anchor="topleft")

            y += line_height

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # close window
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return

            pygame.display.flip()

    def text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple, dest_rect = None, anchor: str = 'center'):
        text_font: Font = pygame.font.Font("./assets/fonts/JetBrainsMono.ttf", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect()
        setattr(text_rect, anchor, text_pos)
        if dest_rect is None:
            dest_rect = text_rect
        self.window.blit(source=text_surf, dest=dest_rect)

def get_formatted_time(elapsed_time):
    elapsed_seconds = elapsed_time // 1000
    mins = elapsed_seconds // 60
    secs = elapsed_seconds % 60
    return f"{mins:02}m{secs:02}s"

def get_formatted_date():
    current_datetime = datetime.datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%y")
    return f"{current_time} | {current_date}"