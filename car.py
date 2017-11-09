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
        print("This car has " + str(self.odometer_reading) + " miles on it")

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
