import pygame

from code.Const import WIN_HEIGHT, WIN_WIDTH, C_BG, C_BLUE_GREY, C_BLACK


class Guide:
    def __init__(self, window):
        self.window = window
        import pygame
        self.surf = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))


    def show(self):
        self.surf.fill(C_BG)
        self.window.blit(self.surf, (0,0))

        border_rect = pygame.Rect((20, 20), (WIN_WIDTH - 40, WIN_HEIGHT - 40))
        pygame.draw.rect(self.window, C_BLUE_GREY, border_rect, 2)

        self.text(30, 'COMO JOGAR', C_BLUE_GREY, (40,40))
        self.text(18, 'Inimigos surgem na tela e o seu foco é evitá-los para manter sua estabilidade.', C_BLACK, (40,80))

        self.text(20, 'INIMIGOS', C_BLUE_GREY, (40,130))
        enemy1 = pygame.image.load('./assets/enemy1.png')
        self.window.blit(enemy1, (40,170))
        self.text(16, 'Ansiedade: movem-se rápido; ao encostar, causam dano continuamente.', C_BLACK, (100,190))
        enemy2 = pygame.image.load('./assets/enemy2.png')
        self.window.blit(enemy2, (40,230))
        self.text(15, 'Procrastinação: são lentas e não causam dano, mas reduzem a velocidade do jogador pela metade.', C_BLACK, (100,240))

        self.text(20, 'HABILIDADES', C_BLUE_GREY, (40, 300))
        enemy1 = pygame.image.load('./assets/skill1.png')
        self.window.blit(enemy1, (40, 340))
        self.text(15, 'Controlar Respiração: quando usada, cria um círculo ao redor do personagem e empurra os inimigos.', C_BLACK, (100, 350))
        enemy2 = pygame.image.load('./assets/skill2.png')
        self.window.blit(enemy2, (40, 420))
        self.text(16, "Reestruturação Cognitiva: transforma os inimigos em 'pensamentos neutros',", C_BLACK, (100, 430))
        self.text(16, 'que podem ser coletados para regenerar a estabilidade do jogador.', C_BLACK, (100, 450))

        neutral_thought = pygame.image.load('./assets/thought.png')
        self.window.blit(neutral_thought, (WIN_WIDTH-140, 440))

        self.text(20, 'Objetivo: sobreviva por 5 minutos. :)', C_BLUE_GREY, (40, 510))


        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # close window
                    quit()  # end pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return

            pygame.display.flip()

    def text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple, dest_rect=None,
             anchor: str = 'topleft'):
        text_font: Font = pygame.font.Font("./assets/fonts/Roboto.ttf", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect()
        setattr(text_rect, anchor, text_pos)
        if dest_rect is None:
            dest_rect = text_rect
        self.window.blit(source=text_surf, dest=dest_rect)