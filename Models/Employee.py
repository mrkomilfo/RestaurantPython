class Employee:
    def __init__(self, surname, name, patronymic, birth_date, position, salary, login, password,
                 menu_access, menu_readonly, staff_access, staff_readonly, orders_access, orders_readonly):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.birth_date = birth_date
        self.position = position
        self.salary = salary
        self.login = login
        self.password = password
        self.menu_access = menu_access
        self.menu_readonly = menu_readonly
        self.staff_access = staff_access
        self.staff_readonly = staff_readonly
        self.orders_access = orders_access
        self.orders_readonly = orders_readonly
