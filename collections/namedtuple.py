from collections import namedtuple
Car = namedtuple('Car','Price Mileage Colour Class')
xyz = Car(Price = 100000, Mileage = 30, Colour = 'Cyan', Class = 'Y')
abc = Car(Class='A', Price = 100000, Mileage = 30, Colour = 'Cyan')
print(xyz)
print(abc)