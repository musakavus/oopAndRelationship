# COMPOSİTİON
# ONE TO ONE RELATİON
# HAS A İLİŞKİSİ VARDIR
# iki class da birbirine bağlıdır. Person classı olmadan 
class ID:
    id_no = None

    def create_id(self, id_number):
        self.id_no = id_number

    def __str__(self):
        return str(self.id_no)

    # def __repr__(self): -> __str__ işlevinin aynısını __repr__ dunder metodu da yapar
    #     return str(self.id_no)


# Bahsettiğim üzere composition miras almak yerine bir classın elamanlarına nesne yoluyla ulaşmamıza sağlar.
# Bu ilişkinin kurulabilmesi için
class Person:
    def __init__(self, name, surname):  # Composition kısmı için en ideal yer constructor bölümüdür
        self.name = name
        self.surname = surname
        self.this_id = ID()  # Class içerisinde self.tihs_id isminde ID() classından referans oluşturuk.

    def __str__(self):  # Bir classın standart str çıktısıdır. !!! AYNI ZAMANDA NESNEDEN STR ÇIKTISI ALMAYA YARAR !!!
        return f'{self.name} {self.surname} {str(self.this_id)}'


p1 = Person('Mina', 'Kavuş')
p1.this_id.create_id(184513515)  # Comp. faydası burda. Referans sayesinde diğer classın özelliğine ulaşabiliyoruz.
# Bu da bize esneklik sağlar
print(p1)  # ___str__ yada __repr__ metodu sayesinde classdan direk string şeklinde çıktı aldık

"""AYNI ŞEYİ KALITIMLA YAPMAYA ÇALIŞALIM"""


class Insan(object):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'{self.name} {self.surname}'


class Kimlik(Insan):
    id_no = None

    def create_id(self, id_number):
        self.id_no = id_number

    def __str__(self):
        return str(self.id_no)


i1 = Insan('Mina', 'Kavuş')
k1 = Kimlik('Mina', 'Kavuş')
k1.create_id(152132315)  # Sıkıntı şurda başlıyor -> k1. dedikten sonra insan sınıfının tüm özelliklerine ulaşabiliyorum
# O yüzden bu programda kalıtımı kullanmak  bize esneklik sağlamaz
print(i1, k1)
