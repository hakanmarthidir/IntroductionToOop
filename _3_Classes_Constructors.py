# nesneler yaratıldıktan sonra sekillenebildigi gibi, ortaya cıkıs anlarında da vermis oldugumuz bilgilere gore
# yaratılabilirler. buna constructor denir.
# bu islemi handle edebilmek için _init_ methodunu kullanmanız yeterlidir.
# ***aslında classımız ortaya cıkıs anında nasıl davransın sorusunun cevabını tanımlarız

class Student:
    StudentNo = ""
    StudentFullname = ""
    StudentLessons = []

    # 1 - empty - varsayılan olarak zaten bu mevcuttur.
    # def __init__(self):
    #     print("empty init")

    # 2 - yaratılıs asamasında dısarıdan parametreler alınır, ancak bos olanı kullanamazsınız.
    # def __init__(self, studentNo, studentFname):
    #     self.StudentFullname = studentFname
    #     self.StudentNo = studentNo
    #     print("full init")

    # 3- nesne yaratılırken parametrelerin tamamı gelmeyebilir, tamamı bos gecilebilir veya hepsi dolu olabilir.
    # gelmeyen parametreler yerine varsayılan olarak deger ataması yapılır ve hem dolu hem de bos constructor kullanılabilir.
    def __init__(self, studentNo=None, studentFname=None):
        self.StudentFullname = studentFname
        self.StudentNo = studentNo
        print("nullable init")

    def AddLessons(self, lessonName):
        self.StudentLessons.append(lessonName)
        print(self.StudentLessons)


s1 = Student()

s2 = Student("123", "hakan hidir")
print(s2.StudentFullname)

s3 = Student("123")
print(s3.StudentNo)
print(s3.StudentFullname)

s4 = Student(studentFname="deneme")
print(s4.StudentFullname)
