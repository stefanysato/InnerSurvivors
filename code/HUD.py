import pygame
from code.Const import WIN_HEIGHT, C_WHITE, ENTITY_SPEED, WIN_WIDTH


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

    def verify_speed_status(self):
        if self.player.is_slowed:
            return 'Lento'
        else:
            return 'Normal'

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

        speed_status = self.verify_speed_status()
        self.text(14, f'Estabilidade: {self.player.stability:.0f}', C_WHITE, (10, 10))
        self.text(14, f'Velocidade: {speed_status}', C_WHITE, (10, 30))
        self.text(14, f'Pensamentos Neutros: {self.player.thoughts_collected}', C_WHITE, (WIN_WIDTH - 10, 30), anchor='topright')

    def text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple,  anchor: str = 'topleft'):
        text_font = pygame.font.Font('./assets/fonts/Roboto.ttf', size=text_size)
        text_surf = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect()
        setattr(text_rect, anchor, text_pos)
        self.window.blit(source=text_surf, dest=text_rect)
