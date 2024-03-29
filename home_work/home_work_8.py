"""
Зробити програму за допомогою функції/функцій у якій потрібно буде вгадувати число.
*Алгоритм програми можна зробити будь-яким, на розсуд виконавця.
Один з варіантів:
- з допомогою зовнішньої функції random створити довільне число, наприклад у діапазоні від 1 до 10.
- У циклі запропонувати користувачеві вгадати загадане число за певну кількість спроб, наприклад 3.
 Якщо введене число угадано, то повідомити про це і запропонувати зіграти заново. Якщо ж не вгадано,
  то повідомити задумане число більше чи менше.
Кожен із пунктів можна організувати як окремої функції, основний алгоритм можна розбити на ще кілька функцій.
"""

import random


def examination(a):
    while True:
        if a.isdigit():
            if 0 <= int(a) <= 10:
                print('Ваше число пройшло перевірку. Ваше число: ', a)
                return a
            else:
                print('Введіть число в діапазоні від 0 до 10')
                a = input('Спробуйте ще раз, введіть число: ')
                continue
        else:
            print('Будь ласка, введіть ціле число!')
            a = input('Спробуйте ще раз, введіть число:')


def game(a, b, c):
    while True:
        c += 1
        if c > 5:
            return b, c
        if int(a) == b:
            return b, c
        elif 0 <= int(a) <= b:
            print(f'Ваше число : {a}. Воно повинно бути більшим, якщо ви хочете перемогти!')
            a = examination(a=input("Введіть ваше число: "))
            continue
        elif 0 <= b <= int(a):
            print(f'Ваше число : {a}. Воно повинно бути меншим, якщо ви хочете перемогти!')
            a = examination(a=input("Введіть ваше число: "))
            continue


comp_number = random.randint(0, 10)
print(comp_number, '- правильна відповідь для перевірки коду')
user_number = input("Введіть ваше ціле число (від 0 до 10): ")
user_number = examination(user_number)
attempts = 0
resultat = game(user_number, comp_number, attempts)
attempts = (resultat[1])
if attempts > 5:
    print(f'Нажаль ви не змогли вгадати {comp_number} число. Ви витратили усі {attempts} спроб')
else:
    print(f'Вітаю , ви вгадали число {resultat[0]}, за {attempts} спроб')
