from prod.model.entity import *


class Kiwi(Product):
    def __init__(self, vitaminC, name="Kiwi"):
        self._name = name
        self._vitaminC = vitaminC

    def __str__(self):
        return (f"{self._name} has {self._vitaminC}mg of vitamin C.")

    @property
    def vitaminC(self):
        return self._vitaminC

    @vitaminC.setter
    def vitaminC(self, vitaminC):
        if vitaminC > 0:
            self._vitaminC = vitaminC
