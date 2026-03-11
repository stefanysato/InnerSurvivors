from code.Const import ENTITY_SPEED

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

    def handle_collision(self):
        for ent1 in self.entities:
            for ent2 in self.entities:
                if ent1 != ent2:
                    pass

    def resolve_collision(self):
        pass

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