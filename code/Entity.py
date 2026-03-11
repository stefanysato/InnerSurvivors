from abc import ABC, abstractmethod


class Entity(ABC):
    def __init__(self, mediator, name, x, y):
        self.mediator = mediator
        self.name = name
        self.x = x
        self.y = y
        self.health = 0

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self, window):
        pass