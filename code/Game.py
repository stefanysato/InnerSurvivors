import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Guide import Guide
from code.Menu import Menu
from code.Score import Score

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption('Inner Survivors')
        icon = pygame.image.load('assets/icon.png')
        pygame.display.set_icon(icon)

    def run(self):
        while True:
            score = Score(self.window)
            guide = Guide(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:
                pygame.mixer.Sound('./assets/sounds/load.wav').play()
                from code.Level import Level
                level = Level(self.window)
                result = level.run()
                if result is not None:
                    final_score, victory, elapsed = result
                    score.save(final_score, victory = victory, elapsed_time=elapsed)

            elif menu_return == MENU_OPTION[1]:
                guide.show()
            elif menu_return == MENU_OPTION[2]:
                score.show()
            elif menu_return == MENU_OPTION[3]:
                pygame.quit()
                quit()

