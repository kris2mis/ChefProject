from prod.model.entity import *


class Banana(Product):
    def __init__(self, name="Banana"):
        self._name = name

    def __str__(self):
        return (f"It is {self._name}.")
