import datetime
import time

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import C_BG, WIN_WIDTH, WIN_HEIGHT, C_BG_WIN, C_BG_LOSE, C_BLACK, C_BLUE_GREY, C_WHITE, \
    SCORE_POS
from code.DBProxy import DBProxy


class Score:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
        self.name = ''
        self.max_chars = 5
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
                self.text(20, self.name, C_BLACK, (WIN_WIDTH / 2, 230), dest_rect=(input_rect.x + 5, input_rect.y + 5))
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

        title_rect = pygame.Rect((0,20), (WIN_WIDTH, 50))
        pygame.draw.rect(self.window, C_BLUE_GREY, title_rect)

        self.text(30, 'SCORE | TOP 10', C_BLACK, (250, 30), anchor='topleft')
        self.text(20, f'Nome       Score       Tempo total     Data', C_BLUE_GREY, (60, 90), anchor='topleft')
        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.show_results()
        db_proxy.close()

        for player_score in list_score:
            id_, name, score, elapsed_time, date = player_score
            self.text(20, f'{name}        {score}         {elapsed_time}          {date}', C_WHITE, SCORE_POS[list_score.index(player_score)], anchor='topleft')

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # close window
                    quit()  # end pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return

            pygame.display.flip()

    def text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple, dest_rect = None, anchor: str = 'center'):
        text_font: Font = pygame.font.SysFont(name="Lucida Console", size=text_size)
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