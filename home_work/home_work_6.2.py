"""
Ввести з клавіатури ціле додатне число n.
Отримати суму кубів всіх натуральних чисел від 1 до n(включаючи n). Винятки становлять усі числа кратні числу 3.
Наприклад, якщо введено число 4, то вам потрібно скласти куби чисел від 1 до 4, виключаючи 3. Тобто: 1 + 8 + 64 = 73
Реалізувати використовуючи цикл for
"""


while True:
    summ_of_cubes = 0
    number_input = (input("Введіть ціле додатне число: "))
    if not number_input.isdigit() or int(number_input) == 0:
        print("Помилка, повторіть введення!")
    else:
        number_input = int(number_input)
        for number in range(0, number_input):
            number += 1
            if number % 3 == 0:
                continue
            summ_of_cubes += number ** 3
        print("summ_of_cubes :", summ_of_cubes)
        exit_g = input("""
Чи бажаєте ви вийти? (Y або Д)
Ваша відповідь: """).upper()
        if exit_g in ("Д", "Y"):
            print('Goodbye!')
            break
