class Product:

    def __init__(self, kcal=0, price=0):
        self.kcal = kcal
        self.price = price

    @property
    def kcal(self):
        return self._kcal

    @kcal.setter
    def kcal(self, kcal):
        if kcal >= 0:
            self._kcal = kcal
        else:
            if not hasattr(self, "_kcal"):
                self._kcal = 0
            else:
                raise ValueError("Calorie content of the dish was wrong")

    @kcal.deleter
    def kcal(self):
        del self._kcal

    def __str__(self):
        return f"kcal = {self._kcal}"

    # @property
    # def price(self):
    #     return self._price
    #
    # @price.setter
    # def price(self, price):
    #     if price >= 0:
    #         self._price = price
    #     else:
    #         if not hasattr(self, "_price"):
    #             self._price = 0
    #
    # @price.deleter
    # def price(self):
    #     del self._price
    #
    # def __str__(self):
    #     return f"price = {self._price}"
