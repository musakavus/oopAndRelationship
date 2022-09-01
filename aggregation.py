# Composition'da Has-a ilişkisi vardır
# Compositiondaki bağ oldukça kuvvetlidir.
""" Örn, üniversite sınıfında fakülte classının nesnesini oluşturduğumuz için universite classı yok olduğunda
    fakülte classı da yok oluyordu. Bu bağı kalıtımdaki IS-A ilişkisi ile karıştırmamak gerekir.
    Kalıtımda fakültede yapacağımız değişiklik üniversiteyi etkileyebilirdi ama compositon'da etkilemez.
"""

# ---> AGGREGATION <---
# AGGERAFATİON'da da HAS-A ilişkisi vardır ama bağlı classın referans ana classta olusturulmasına gerek yoktur.
# Bu yüzden bağlı class ana classa bağlı olmadan da çalışabilir.
"""
a1 = Akademisyen('Hüseyin Savran', 2022) 
a1.akademisyen_ekle()
b1 = Bolum('Bilgisayar Mühendisliği')
b1.bolum_ekle(a1) --> # Burda parametre olarak ana classtaki nesne yerine
                      başka parametre versen de çalışır.Yani her türlü çalışabilir. Bu yüzden ana classa bağlı değildir
"""

from abc import ABC, abstractmethod


class UniAbstract(ABC):
    def akademisyek_ekle(self):
        pass

    def bolum_ekle(self, akademisyen_adi):
        pass


class Bolum(UniAbstract):

    def __init__(self, bolum_adi):
        self.bolum_adi = bolum_adi

    def bolum_ekle(self, akademisyen_adi):
        self.akademisyen_adi: Akademisyen = akademisyen_adi
        # sayi : int yaparak sayinin int cinsinden olduğunu belirtirim
        # aynı şekilde akademisyen_adi : akademisyen dersem bununda Akademisyen sınıfı cinsinden olduğunu blrtmiş olurum

    def __repr__(self):
        return f'{self.akademisyen_adi} \n{self.bolum_adi}'


class Akademisyen(UniAbstract):
    temp = None

    def __init__(self, akademisyen_adi, experience_year):
        self.akademisyen_adi = akademisyen_adi
        self.experience_year = experience_year

    def akademisyen_ekle(self):
        if self.experience_year > 10:
            self.temp = f'Prof. {self.akademisyen_adi}'

        elif 10 >= self.experience_year >= 5:
            self.temp = f'Dr. {self.akademisyen_adi}'

        else:
            self.temp = f'Ogr {self.akademisyen_adi}'

    def __repr__(self):
        return str(self.temp)


a1 = Akademisyen('Hüseyin Savran', 2022)
a1.akademisyen_ekle()
b1 = Bolum('Bilgisayar Mühendisliği')
b1.bolum_ekle(a1)
print(b1)

print(b1.akademisyen_adi.akademisyen_adi)  # Görüldüğü üzere nesneler yoluyla ulaşım sağlayabiliyorum
print(b1.akademisyen_adi.experience_year)
