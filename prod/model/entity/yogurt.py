from prod.model.entity import *


class Yogurt(Product):
    def __init__(self, volume):
        self._volume = volume

    def __str__(self):
        return (f"{self._volume} ml of yougurt.")

