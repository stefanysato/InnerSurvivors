import pygame
from code.Const import WIN_HEIGHT, C_WHITE


class HUD:
    def __init__(self, player, window):
        self.player = player
        self.window = window

        self.skill_icons = [
            pygame.image.load('./assets/skill1.png').convert_alpha(),
            pygame.image.load('./assets/skill2.png').convert_alpha()
        ]

        self.positions = [
            (40, WIN_HEIGHT - 80),
            (100, WIN_HEIGHT - 80)
        ]

    def draw(self, window):
        for i, skill in enumerate(self.player.skills):
            icon = self.skill_icons[i]
            x, y = self.positions[i]

            window.blit(icon, (x, y))


            progress = skill.get_cooldown_progress()
            cooldown_ratio = 1 - progress

            if cooldown_ratio > 0:
                width, height = icon.get_size()

                overlay_height = height * cooldown_ratio

                overlay = pygame.Surface((width, overlay_height))
                overlay.fill((0, 0, 0))
                overlay.set_alpha(200)

                window.blit(overlay, (x, y))

        self.text(14, f'Estabilidade: {self.player.stability:.0f}', C_WHITE, (10, 10))
        self.text(14, f'Velocidade: {self.player.current_speed}', C_WHITE, (10, 30))


    def text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font = pygame.font.SysFont(name="Verdana", size=text_size)
        text_surf = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
