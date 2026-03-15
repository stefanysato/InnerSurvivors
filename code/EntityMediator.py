from code.NeutralThought import NeutralThought


class EntityMediator:
    def __init__(self):
        self.player = None
        self.enemies = []
        self.entities = []
        self.thoughts = []

    def register(self, entity):
        if entity.type == "player":
            self.player = entity

        if entity.type == "enemy":
            self.enemies.append(entity)

        if entity.type == "thought":
            self.thoughts.append(entity)

        self.entities.append(entity)

    def remove(self, entity):
        self.entities.remove(entity)

    def get_player(self):
        return self.player

    def get_enemies(self):
        return self.enemies

    # player skills
    def push_enemies(self, player):
        for enemy in self.enemies:
            distance = enemy.position.distance_to(self.player.position)

            if distance < player.breath.radius:
                enemy.status["repel"] = True
            else:
                enemy.status["repel"] = False

    def transform_to_neutral(self, enemy):
        for enemy in self.enemies:
            x = enemy.x
            y = enemy.y

            self.remove(enemy)

            neutral = NeutralThought(x, y, self)
            self.register(neutral)