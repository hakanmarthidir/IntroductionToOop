# public private protected gibi access modifier yapılar pythonda yoktur.
class Human:
    fullName = ""
    age = 0
    runningSpeed = 0
    __health = 100

    def __init__(self, humanFullname=None, humanAge=0):
        self.fullName = humanFullname
        self.age = humanAge

    def __str__(self):
        return self.fullName

    def Run(self):
        self.runningSpeed += 1
        self.__health += 5

    def DoWork(self):
        self.runningSpeed -= 1
        self.__health -= 2

class Doctor(Human):
    hospital = ""
    level = "Dr."

    def Run(self):
        self.runningSpeed += 2
        # self.__health bu deger ulasamayız. __ seklinde işaretlendigi için sadece o class içerisinde kullanılır.

    def __str__(self):
        return self.hospital

    def DoWork(self):
        self.runningSpeed -= 2

class Cop(Human):
    policeStation = ""
    killCount = 0

    def Run(self):
        self.runningSpeed += 3

    def __str__(self):
        return self.policeStation

class Robot:
    hasAI = False

    def __str__(self):
        return self.hasAI

class RoboCop(Cop, Robot):
    Material = ""

    def __str__(self):
        return self.Material

# robocop nesnesi içerisinde human, cop ve kendi ozelliklerini goruruz.
roboCop = RoboCop();
roboCop.policeStation = "New York"
roboCop.hasAI = True
roboCop.Material = "Lithium"
print(roboCop)
print("{} - {}".format(roboCop.policeStation, roboCop.fullName))
