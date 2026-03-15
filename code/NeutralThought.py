from code.Entity import Entity


class NeutralThought(Entity):
    def __init__(self, name, mediator, x, y):
        super().__init__(mediator, name, x, y)
        self.type = 'thought'

    def update(self):
        pass

    def draw(self, window):
        pass
