class ID:
    id_no = None

    def create_id(self, id_number):
        self.id_no = id_number

    def __str__(self):
        return str(self.id_no)

    # def __repr__(self): -> __str__ işlevinin aynısını __repr__ dunder metodu da yapar
    #     return str(self.id_no)


class Person:
    def __init__(self, name, surname):  # Composition kısmı için en ideal yer constructor bölümüdür
        self.name = name
        self.surname = surname
        self.this_id = ID()  # Class içerisinde self.tihs_id isminde ID() classından referans oluşturuk.

    def __str__(self):  # Bir classın standart str çıktısıdır.
        return f'{self.name} {self.surname} {str(self.this_id)}'


p1 = Person('Mina', 'Kavuş')
p1.this_id.create_id(184513515)
print(p1)
