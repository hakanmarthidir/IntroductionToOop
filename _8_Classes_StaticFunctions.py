class MyMethods:
    @classmethod
    def Divide(self, number1, number2):
        return float(number1/ number2)

result = MyMethods.Divide(23,3)
print(result)