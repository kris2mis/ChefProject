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

        #переопределеили

        # for i in range(dish.size()):
        #     product = dish.get(i)
        #     if isinstance(product, Product):
        #         total += product.kcal
        #
        # return total



    # @staticmethod
    # def calculate_total_price(basket):
    #     return 0
    #     # if not isinstance(basket, Basket):
    #     #     return -1
    #     #
    #     # total = 0
    #     #
    #     # for i in range(basket.size()):
    #     #     product = basket.get(i)
    #     #     if isinstance(product, Product):
    #     #         total += product.price
    #     #
    #     # return total
