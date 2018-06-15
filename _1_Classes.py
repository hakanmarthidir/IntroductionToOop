#OOP -> Object Oriented Programming
#nesneye dayalı programlamanın en temel unsuru classtır.
#belirli bir konudaki, birbiri ile ilişkili kodların bir arada tutuldugu alanlardır.


class FirstClass:
    pass


# Instance - Bir ornek olusturma
# Yukarıda tanımladıgınız sablona gore memory uzerinde yer kaplayan bir nesne olusturulur.
# Her yeni nesne olusturdugunuzda bu nesnelerin farklı memory lokasyonlarında yer aldıgını bilmelisiniz.
# birbirlerinden bagımsızdırlar.

# Ek: pass anahtar kelimesi hic bir sey yapma anlamında kullanılır.
# donguler içerisinde de kullanabilirsiniz.

student = FirstClass()
print(student)

student2 = FirstClass()
print(student2)

#her iki nesneyi print ettigimizde farklı hex kodlarına sahip 2 nesnenin var oldugunu goruruz.
