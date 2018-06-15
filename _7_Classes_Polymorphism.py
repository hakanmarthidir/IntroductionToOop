# import Classes_Demo
# from _6_Classes_Demo import Truck
from _6_Classes_Demo import *

"""bazı modullerin içerisinde cok fazla class olabiliyor. bunların tamamını kullanıma acmak yerine
sadece kullanmak istediginiz nesneyi cagirabilirsiniz."""


# Polymorphism
def GetGasoline(c):
    c.TakeGasoline(20)


car = Car()
truck = Truck()
bus = Bus()

GetGasoline(car)
GetGasoline(truck)
GetGasoline(bus)
