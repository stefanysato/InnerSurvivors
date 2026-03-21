import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Menu import Menu
from code.Score import Score

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption('INNER SURVIVORS')

    def run(self):
        while True:
            score = Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:
                from code.Level import Level
                level = Level(self.window)
                result = level.run()
                if result is not None:
                    final_score, victory = result
                    score.save(final_score, victory = victory)

            elif menu_return == MENU_OPTION[1]:
                score.show()
            elif menu_return == MENU_OPTION[4]:
                pygame.quit()
                quit()

