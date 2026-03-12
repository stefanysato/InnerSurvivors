from code.Const import ENTITY_SPEED, WIN_WIDTH, WIN_HEIGHT
from code.Player import Player


class EntityMediator:
    def __init__(self):
        self.player = None
        self.entities = []

    def register(self, entity):
        self.entities.append(entity)

        if entity.type == "player":
            self.player = entity

    def remove(self, entity):
        self.entities.remove(entity)

    def get_player(self):
        if self.player:
            return self.player

    # player skills
    def skill1(self):
        pass

    def cognitive_restructure(self, player):
        pass

    def skill3(self):
        pass