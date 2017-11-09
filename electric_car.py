from car import Car


class Battery():
    """
    Class that describes batteries
    """
    def __init__(self, battery_size=70):
        """
        Battery size
        :param battery_size: int
        """
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery"""
        print("This car has a {}-kWh battery".format(self.battery_size))

    def get_range(self):
        """
        Gets range of battery
        :return: str
        """
        mile_range = 0
        if self.battery_size == 70:
            mile_range = 240
        elif self.battery_size == 85:
            mile_range = 270

        message = "This car can go approximately " + str(mile_range) + " miles on a full charge"
        print(message)


class ElectricCar(Car):
    """
    Electric Car, inherits from Car
    """

    def __init__(self, make, model, year):
        """
        Represent aspects of a car, specific to electric cars
        :param make: str
        :param model: str
        :param year: int
        """
        super().__init__(make, model, year)
        self.battery = Battery()