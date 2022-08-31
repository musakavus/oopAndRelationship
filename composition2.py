# ONE TO ONE RELATİON

from abc import ABC, abstractmethod


class University(ABC):
    def create_book(self): pass

    def add_book(self, book_name, book_id): pass  # Normal metodda hangi parametreler varsa abs class içindede olmalı


class Library(University):
    kitap = None

    def __init__(self, lib_name, lib_id):
        self.lib_name = lib_name
        self.lib_id = lib_id

    def create_book(self):  # Daha önce contructor içerisinde referans oluşturmuştuk şimdi normal metod içerisinde
        # Hatırlatmakta fayda var en mantıklısı constructor içerisinde oluşturmaktır.
        self.kitap = Book()

    def __repr__(self):
        return f'Kütüphane Adı: {self.lib_name}  \nKütüphane Id:{str(self.lib_id)} \nKitap {self.kitap}'


class Book(University):

    def __init__(self):
        self.book_name = None
        self.book_id = None

    def __repr__(self):
        return f'Kitap ismi: {self.book_name} \nKitap Id: {str(self.book_id)}'


l1 = Library('Yılmaz Güney', 15631)
l1.create_book()
l1.kitap.book_id = 13252
l1.kitap.book_name = 'Denizler Altında 80 bin Fersah'
print(l1)
