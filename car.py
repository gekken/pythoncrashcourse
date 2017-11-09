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
