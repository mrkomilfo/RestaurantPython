from Models.Dish import Dish


class Menu(dict):
    def add(self, dish):
        self.setdefault(dish.name, dish)


def remove(self, key):
    self.pop(key)

@staticmethod
def get_start_menu():
    start_menu = Menu()
    start_menu.add(Dish("Холодные закуски", "Салат Цезарь", 2.9, 150))
    start_menu.add(Dish("Холодные закуски", "Салат Оливье", 3.4, 150))
    start_menu.add(Dish("Первое блюдо", "Суп харчо", 3.5, 300))
    start_menu.add(Dish("Первое блюдо", "Красный борщ", 3, 300))
    start_menu.add(Dish("Гарниры", "Пюре картофельное", 2.3, 250))
    start_menu.add(Dish("Гарниры", "Плов с бараниной", 5, 280))
    start_menu.add(Dish("Горячие блюда", "Драники со сметаной", 2.5, 280))
    start_menu.add(Dish("Горячие блюда", "Котлета по-киевски", 4.5, 120))
    start_menu.add(Dish("Напитки", "Чай", 2, 250))
    start_menu.add(Dish("Напитки", "Кофе", 3, 250))
    start_menu.add(Dish("Десерты", "Тирамису", 3.5, 180))
    start_menu.add(Dish("Десерты", "Эклер", 2.5, 70))
    return start_menu
