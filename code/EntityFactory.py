from code.Enemy import Enemy
from code.NeutralThought import NeutralThought
from code.Player import Player

class EntityFactory:
    def __init__(self, mediator):
        self.mediator = mediator

    def create_player(self, name: str, x, y) -> Player:
        player = Player(self.mediator, name, x, y)
        self.mediator.register(player)
        return player

    def create_enemy(self, name: str, x, y):
        enemy = Enemy(self.mediator, name, x, y)
        self.mediator.register(enemy)
        return enemy

    def create_neutral_thought(self, x, y):
        thought = NeutralThought(self.mediator, x, y)
        self.mediator.register(thought)
        return thought
