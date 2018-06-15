# Araba base class olacak sekilde Otobus ve Tır classlarını olusturunuz.
class Car(object):
    Brand = ""
    Model = ""
    Year = 0
    Gasoline = 0

    def TakeGasoline(self, litres):
        self.Gasoline += litres


class Bus(Car):
    Departure = ""
    Arrival = ""


class Truck(Car):
    MaxCarriage = 0
