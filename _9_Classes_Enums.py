from enum import Enum, unique


@unique
class Colors(Enum):
    Red = 1,
    Yellow = 2
    Blue = 3


class Dress(object):
    DressColor = Colors.Red

    def __init__(self):
        print("{}".format(self.DressColor.name))
        print(self.DressColor.value)


dress = Dress()
