import pymongo as pm
from Models.Menu import Menu
from Models.Staff import Staff
from Models.Dish import Dish
from Models.Employee import Employee
from Models.Order import Order
from Models.Bill import Bill
from Models.Section import Section


class dbHandler:
    connection = pm.MongoClient()
    db = connection["restaurant"]
    account = None

    @staticmethod
    def get_menu():
        collection = dbHandler.db["menu"].find()
        menu = Menu()
        for dish in collection:
            menu.add(Dish(dish["type"], dish["name"], dish["price"], dish["energy"], dish["output"]))
        return menu

    @staticmethod
    def get_staff():
        collection = dbHandler.db["staff"].find()
        staff = Staff()
        for employee in collection:
            staff.recruit(Employee(employee["surname"], employee["name"], employee["patronymic"], employee["birth_date"],
                                   employee["position"], employee["salary"], employee["login"], employee["password"],
                                   employee["menu_access"], employee["menu_readonly"], employee["staff_access"],
                                   employee["staff_readonly"], employee["orders_access"], employee["orders_readonly"]))
        return staff

    @staticmethod
    def login(login, password):
        account = dbHandler.db["staff"].find_one({"login": login, "password": password})
        if not account:
            return False
        dbHandler.account = Employee(account["surname"], account["name"], account["patronymic"], account["birth_date"],
                                     account["position"], account["salary"], account["login"], account["password"],
                                     account["menu_access"], account["menu_readonly"], account["staff_access"],
                                     account["staff_readonly"], account["orders_access"], account["orders_readonly"])
        return True

    @staticmethod
    def get_account():
        return dbHandler.account

    @staticmethod
    def add_dish(dish):
        dbHandler.db["menu"].insert_one({"type": dish.dish_type, "name": dish.name, "price": dish.price,
                                         "energy": dish.energy, "output": dish.output})

    @staticmethod
    def remove_dish(name):
        dbHandler.db["menu"].delete_one({"name": name})

    @staticmethod
    def add_employee(employee):
        dbHandler.db["staff"].insert_one({"surname": employee.surname, "name": employee.name, "patronymic": employee.patronymic,
                                          "birth_date": employee.birth_date, "position": employee.position,
                                          "salary": employee.salary, "login": employee.login, "password": employee.password,
                                          "menu_access": employee.menu_access, "menu_readonly": employee.menu_readonly,
                                          "staff_access": employee.staff_access, "staff_readonly": employee.staff_readonly,
                                          "orders_access": employee.orders_access, "orders_readonly": employee.orders_readonly})

    @staticmethod
    def remove_employee(login):
        dbHandler.db["staff"].delete_one({"login": login})

    @staticmethod
    def get_orders():
        collection = dbHandler.db["orders"].find()
        orders = dict()
        for order in collection:
            orders.setdefault(order["id"], dbHandler.get_order(order["id"]))
        return orders

    @staticmethod
    def get_order(id):
        bill = Bill()
        collection = dbHandler.db["order" + id].find()
        for section_doc in collection:
            dish = Dish(section_doc["type"], section_doc["name"], section_doc["price"], section_doc["energy"], section_doc["output"])
            section = Section(dish)
            section.number = section_doc["number"]
            bill.add(section)
        time = dbHandler.db["orders"].find_one({"id": id})["time"]
        return Order(id, time, bill)


    @staticmethod
    def add_order(order):
        dbHandler.db["orders"].insert_one({"id": order.id, "time": order.time})
        for section in order.values():
            dbHandler.db["order" + order.id].insert_one({"type": section.dish_type, "name": section.name,
                                                         "price": section.price, "energy": section.energy,
                                                         "output": section.output, "number": section.number})

    @staticmethod
    def close_order(id):
        dbHandler.db["orders"].delete_one({"id": id})
        dbHandler.db["order" + id].drop()

    @staticmethod
    def change_password(login, password):
        dbHandler.db["staff"].update({"login": login}, {"$set": {"password": password}})
