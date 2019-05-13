class Dish:
    def __init__(self,  dish_type, name, price, out):
        self.__dish_type = dish_type
        self.__name = name
        self.__price = price
        self.__out = out

    @property
    def dish_type(self):
        return self.__dish_type

    @dish_type.setter
    def dish_type(self, dish_type):
        self.__dish_type = dish_type

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    @property
    def out(self):
        return self.__out

    @out.setter
    def out(self, out):
        self.__out = out




