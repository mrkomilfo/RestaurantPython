from Models.Employee import Employee
import datetime


class Staff(dict):
    def recruit(self, employee):
        self.setdefault(employee.login, employee)

    def dismiss(self, login):
        self.pop(login)

    @staticmethod
    def get_start_staff():
        start_staff = Staff()
        employee = Employee("Дорофеев", "Валентин", "Игоревич", datetime.date(2000, 2, 17), "Администратор",
                            500, "komilfo", "1312", True, False, True, False, True, False)
        start_staff.recruit(employee)
        return start_staff
