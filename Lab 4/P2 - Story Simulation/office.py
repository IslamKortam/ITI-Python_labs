
class Office:
    def __init__(self, name, employees):
        self.name = name
        self.employees = employees

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, n):
        if isinstance(n, str):
            self.__name = n
        else:
            raise Exception("Name must be a string")

    @property
    def employees(self):
        return self.__employees
    @employees.setter
    def employees(self, e):
        if isinstance(e, list):
            self.__employees = e
        else:
            raise Exception("Employees must be of a class List")


    def get_all_get_employee(self):
        pass

    def hire(self):
        pass

    def fire(self):
        pass

    def calculate_lateness(self):
        pass

    def deduct(self):
        pass

    def reward(self):
        pass

