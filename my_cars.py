from car import Car
from electric_car import ElectricCar

my_beetle = Car('volkswagen', 'new beetle', 2016)
my_tesla = ElectricCar('tesla', 'roadster', 2017)

print(my_beetle.get_descriptive_name())
print(my_tesla.get_descriptive_name())