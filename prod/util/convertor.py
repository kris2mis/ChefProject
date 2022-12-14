from prod.model.entity import *


class Convertor:

    @staticmethod
    def convert_to_string(salads):
        s = "List of salads:\n"

        if not isinstance(salads, (list, tuple)):
            return "List is empty"

        for salad in salads:
            if isinstance(salad, Dish):
                s += "\n" + str(salad)

        return s