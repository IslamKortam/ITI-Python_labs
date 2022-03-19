

class Person:
    def __init__(self, name, money, mood, healthCare):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthCare = healthCare

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
    def money(self):
        return self.__money
    @money.setter
    def money(self, m):
        if isinstance(m, int) and m >= 0:
            self.__money = m
        else:
            raise Exception("Money must be an Integer >= 0")

    @property
    def mood(self):
        return self.__mood
    @mood.setter
    def mood(self, m):
        acceptedMoods = ["happy", "tired", "lazy"]
        if isinstance(m, str):
            m = m.lower()
            if m in acceptedMoods:
                self.__mood = m
            else:
                raise Exception(f"Undefined mood, mood must be one of {acceptedMoods}")
        else:
            raise Exception("Mood must be a String")

    @property
    def healthCare(self):
        return self.__healthCare
    @healthCare.setter
    def healthCare(self, h):
        if isinstance(h, int):
            if h >= 0 and h <= 100:
                self.__healthCare = h
            else:
                raise Exception("Health Care must be between 0 and 100 inclusive")
        else:
            raise Exception("Health Care must be an Integer")

    def __str__(self):
        return self.name + ":" + str(self.money) + ":" + self.mood + ":" + str(self.healthCare)

    def sleep(self):
        pass

    def eat(self):
        pass

    def buy(self):
        pass
