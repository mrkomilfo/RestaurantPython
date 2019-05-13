import Models.Dish as Dish


class Section(Dish):
    def __init__(self, dish):
        self.__name = dish.name
        self.__out = dish.out
        self.__price = dish.price
        self.__number = 1

    @property
    def number(self):
        return self.__number

    def increment(self):
        self.__number += 1

    def decrement(self):
        self.__number -= 1

