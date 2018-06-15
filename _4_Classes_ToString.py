class Footballer(object):
    NameSurname = ""
    Country = ""
    Number = 0
    Position = ""

    def __str__(self):
        return (self.NameSurname + " " + self.Country)

    def __del__(self):
        print("im dead")

forward = Footballer()
forward.NameSurname = "aaa bbb"
forward.Country = "Brezilya"
print(forward)
del forward

# Footballer nesnesinden yeni bir ornek olusturdugumuzda ve bu nesneyi print etmek istedigimizde hangi ozellikler ekrana
# getirecegine karar veremedigi için varsayılan olarak belirtilmis bir cıktı uretir.
# print ile ortaya cıkan varsayılan metinde hangi tipte oldugunu ve memorydeki adresi gorebilirsiniz.
# bunu degistirmek için __str__ methodunu override ederiz.