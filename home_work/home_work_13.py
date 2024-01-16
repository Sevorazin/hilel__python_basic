"""
Написати декоратор до 2-х будь-яких функцій, який би рахував та виводив час їх виконання.
Підсказка:
from datetime import datetime
now = datetime.now()
"""

from datetime import datetime

def decorator (func):
    def wraper (*args,**kwargs):
        start = datetime.now()
        result = func(*args,**kwargs)
        print(f'На виконання функції довелось витратити {datetime.now() - start} ')
        return result
    return wraper


@decorator
def home_work_4():
    exit = 1
    while exit == 1:
        name = input("Введіть ваше ім'я: ")
        age = input("Введіть ваш вік: ")

        if not age.isdigit() or int(age) == 0:
            print("Помилка, повторіть введення!")
        elif 0 < int(age) < 10:
            print("Привіт, шкет ", name)
        elif 10 <= int(age) <= 18:
            print("Як справи, ", name)
        elif 18 < int(age) < 100:
            print("Що бажаєте", name)
        else:
            print(name, "ви брешете - у наш час стільки не живуть...")
        exit_1 = input("""
    Чи бажаєте ви вийти? (Y або Д)
    Ваша відповідь: """).upper()
        if exit_1 in ("Д", "Y"):
            break


@decorator
def home_work_6_1():
    exit = 1
    number = 0
    summ_of_cubes = 0

    while exit:
        number_input = (input("Введіть ціле додатне число: "))
        if not number_input.isdigit() or int(number_input) == 0:
            print("Помилка, повторіть введення!")
        else:
            number_input = int(number_input)
            while number_input > number:
                number += 1
                if number % 3 == 0:
                    continue
                summ_of_cubes += number ** 3

            print("summ_of_cubes :", summ_of_cubes)
            exit = input("""
    Чи бажаєте ви вийти? (Y або Д)
    Ваша відповідь: """).upper()
            if exit in ("Д", "Y"):
                print('Goodbye!')
                break


home_work_4()
home_work_6_1()