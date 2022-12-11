import unittest

from prod.model.entity import *
from prod.model.logic import *


class TestSaladManager(unittest.TestCase):
    def test_calculate_total_calories_basic(self):
        dish = Dish()
        dish.add(Product(1))
        dish.add(Product(2))
        dish.add(Product(3))
        expected = 6

        actual = SaladManager.calculate_total_calories(dish)

        self.assertEqual(expected, actual)

    def test_calculate_total_calories_with_incorrect_data(self):
        expected = -1
        actual = SaladManager.calculate_total_calories(100)
        self.assertEqual(expected, actual)

    def test_calculate_total_calories_with_empty_dish(self):
        expected = 0
        actual = SaladManager.calculate_total_calories(Dish())
        self.assertEqual(expected, actual)

    def test_calculate_total_calories_with_only_one_product(self):
        dish = Dish()
        product = Product(15)
        dish.add(product)
        expected = product.kcal
        actual = SaladManager.calculate_total_calories(dish)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
