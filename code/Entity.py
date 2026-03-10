from abc import ABC, abstractmethod


class Entity(ABC):
    def __init__(self, mediator, name, position: tuple):
        self.mediator = mediator
        self.name = name
        self.position = position
        self.health = 0

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self, window):
        pass