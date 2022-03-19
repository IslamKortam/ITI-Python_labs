class Car:
    def __init__(self, name, fuelRate, velocity):
        self.name = name
        self.fuelRate = fuelRate
        self.velocity = velocity

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
    def fuelRate(self):
        return self.__fuelRate
    @fuelRate.setter
    def fuelRate(self, rate):
        if isinstance(rate, float) or isinstance(rate, int):
            self.__fuelRate = rate
        else:
            raise Exception("Fuel rate must be an (Int or Float)")

    @property
    def velocity(self):
        return self.__velocity
    @velocity.setter
    def velocity(self, v):
        if isinstance(v, int) or isinstance(v, float):
            self.__velocity = v
        else:
            raise Exception("velocity must be an (Int or Float")

    def run(self):
        pass

    def stop(self):
        pass
