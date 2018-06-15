# Herhangi bir classı tanımlarken dusunmemiz gereken en onemli unsurlar;
#  1- bu classın hangi ozellikleri olur.
#  2- bu class hangi eylemleri gerceklestirebilir.
# Her uygulama icerisinde class olacak diye bir durum yoktur. Uygulamalarımız içerisindeki kodları mantıksal olarak
# gruplandırmak, (alısveris senaryosunda oldugu gibi ürün ile ilgili kodlar ürün clasında,
# satın alma işlemi ile ilgili kodlar ayrı bir classta tutulabilir.)
# daha rahat kodları okuyabilmek ve degistirebilmek için classlarımızı yaratırız.


class Person:
    PersonIdentityNo = ""
    PersonName = ""
    PersonSurname = ""
    PersonAge = 0

    def SayYourFullName(self):
        print(self.PersonName + " " + self.PersonSurname)


myPerson = Person()
myPerson.PersonName = "hakan"
myPerson.PersonSurname = "hidir"
myPerson.PersonAge = 37
myPerson.PersonIdentityNo = "123456789A"
myPerson.SayYourFullName();
