from electric_car import ElectricCar

from Ch9.car import Car

my_beetle = Car('volkswagen', 'new beetle', 2016)
my_tesla = ElectricCar('tesla', 'roadster', 2017)

print(my_beetle.get_descriptive_name())
print(my_tesla.get_descriptive_name())