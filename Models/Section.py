import Models.Dish as Dish


class Section(Dish.Dish):
    def __init__(self, dish):
        self.dish_type = dish.dish_type
        self.name = dish.name
        self.output = dish.output
        self.energy = dish.energy
        self.price = dish.price
        self.number = 1

    def get_cost(self):
        return self.number * self.price

    def increment(self):
        self.number += 1

    def decrement(self):
        self.number -= 1

