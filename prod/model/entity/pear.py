from prod.model.entity import *


class Pear(Product):
    def __init__(self, count):
        self._name = count

    def __str__(self):
        return (f"You choose {self._count} pears.")

