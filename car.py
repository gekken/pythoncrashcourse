class Car():
    """
    A simple attempt to represent a car
    """

    def __init__(self, make, model, year):
        """
        Initialize attributes to make a car
        :param make: str
        :param model: str
        :param year: str
        """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """
        Return neatly-formatted name
        :return: str - formatted name, Title Case
        """
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """
        read odometer
        :return: str - odometer reading
        """
        print("This car has {:d} miles on it".format(self.odometer_reading))

    def update_odometer(self, milage):
        """
        set the odometer
        Reject the change if we attempt to roll it back
        :param milage: int
        :return: return odometer reading
        """
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """
        increment odometer by miles
        :param miles: int
        :return: odometer_reading is incremented
        """
        self.odometer_reading += miles


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



my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.read_odometer()
my_new_car.update_odometer(22)

my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()

my_tesla = ElectricCar('tesla', 'model s', 2017)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()

my_tesla.battery.get_range()