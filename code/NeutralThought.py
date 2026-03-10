from code.Entity import Entity


class NeutralThought(Entity):
    def __init__(self, name, mediator):
        super().__init__(self, name, mediator)
        self.type = 'thought'

    def update(self):
        pass

    def draw(self, window):
        pass
