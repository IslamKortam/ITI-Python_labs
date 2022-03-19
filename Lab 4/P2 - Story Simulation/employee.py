from helpingMethods import *
from car import Car
from person import Person

class Employee(Person):
    def __init__(self, name, money, mood, healthCare, id, car, email, salary, distanceToWork):
        super().__init__(name, money, mood, healthCare)
        self.id = id
        self.car = car
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, i):
        if isinstance(i, int) and i >= 0:
            self.__id = i
        else:
            raise Exception("ID must be an Integer >= 0")

    @property
    def car(self):
        return  self.__car
    @car.setter
    def car(self, c):
        if isinstance(c, Car):
            self.__car = c
        else:
            raise Exception("car must be of a class Car")



    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, e):
        if isinstance(e, str):
            if validateEmail(e):
                self.__email = e
            else:
                raise Exception("Not a valid Email")
        else:
            raise Exception("Email must be a String")

    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self, s):
        if isinstance(s, int) and s >= 1000:
            self.__salary = s
        else:
            raise Exception("Slary must be an Int >= 1000")

    @property
    def distanceToWork(self):
        return self.__distanceToWork
    @distanceToWork.setter
    def distanceToWork(self, d):
        if (isinstance(d, int) or isinstance(d, float) ) and d > 0:
            self.__distanceToWork = d
        else:
            raise Exception("distanceToWork must be an (Int or Float) Larger than 0")

    def work(self):
        pass

    def drive(self):
        pass

    def refuel(self):
        pass

    def send_email(self):
        pass


