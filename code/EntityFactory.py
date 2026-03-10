from code.Enemy import Enemy
from code.NeutralThought import NeutralThought
from code.Player import Player

class EntityFactory:
    def __init__(self, mediator):
        self.mediator = mediator

    def create_player(self, name: str, pos: tuple) -> Player:
        player = Player(self.mediator, name, pos)
        self.mediator.register(player)
        return player

    def create_enemy(self, name: str, pos: tuple):
        enemy = Enemy(self.mediator, name, pos)
        self.mediator.register(enemy)
        return enemy

    def create_neutral_thought(self, pos: tuple):
        thought = NeutralThought(self.mediator, pos)
        self.mediator.register(thought)
        return thought
