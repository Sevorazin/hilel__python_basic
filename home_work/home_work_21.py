"""
Створити батьківський клас auto, який має атрибути:
brand, age, cоlor, mark і weight.
А також методи: move, birthday і stop.
Методи move і stop виводять повідомлення на екран «move» та «stop», а birthday збільшує атрибут age на 1.
Атрибути brand, age та mark є обов'язковими під час оголошення об'єкта.
"""


class Auto:
    def __init__(self, brand, age, mark, color=None, weight=None):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    def move(self):
        print("move")

    def stop(self):
        print("stop")

    def birthday(self):
        self.age += 1


car1 = Auto(brand="Toyota", age=5, mark="Sedan", color="Blue", weight=1500)
car1.move()
car1.stop()
print(f"Before birthday: {car1.age} years old")
car1.birthday()
print(f"After birthday: {car1.age} years old")
