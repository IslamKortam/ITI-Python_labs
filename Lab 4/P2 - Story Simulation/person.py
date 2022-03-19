

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

    def sleep(self, hours):
        if (isinstance(hours, int) or isinstance(hours, float)) and hours >= 0:
            if hours == 7:
                self.mood = "happy"
            elif hours < 7:
                self.mood = "tired"
            else:
                self.mood = "lazy"
        else:
            raise Exception("Hours must be (int or Float) >= 0")

    def eat(self, meals):
        if isinstance(meals, int) and meals >= 0:
            if meals == 3:
                self.healthCare = 100
            elif meals == 2:
                self.healthCare = 75
            elif meals == 1:
                self.healthCare = 50
            elif meals == 0 or meals > 3:
                self.healthCare = 25
        else:
            raise Exception("meals must be (int) >= 0")

    def buy(self, itemsCount):
        if isinstance(itemsCount, int) and itemsCount >= 0:
            totalPrice = itemsCount * 10
            if totalPrice <= self.money:
                self.money = self.money - totalPrice
            else:
                raise Exception("Not enough money to buy these items")
        else:
            raise Exception("Items count must be a positive integer")
