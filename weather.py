from helper_functions import reader


class weather:
    def __init__(self, name):
        self.animation, _ = reader(name, True)

    def update(self):
        self.animation = self.animation.next
        return self.animation.value[True]