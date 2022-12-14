from prod.model.entity import *


class SaladManager:
    @staticmethod
    def calculate_total_calories(dish):

        if not isinstance(dish, Dish):
            return -1

        total = 0

        for pr in dish:
            if isinstance(pr, Product):
                total += pr.kcal
        return total

    @staticmethod
    def find_highest_calorie_salad(fruits):
        pass
