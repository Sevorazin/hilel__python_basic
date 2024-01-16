"""
Запросити у користувача число. Якщо введено не ціле число, видати на екран повідомлення: "не вірне введення"\
Якщо введено число, то за допомогою тернарного виразу обчислити яке число введено – парне чи непарне.
 (Умова перевірки на парність: х % 2)
Після цього вивести на екран: "Ви ввели парне число" або "Ви ввели непарне число".
 При цьому вивід необхідно організувати у вигляді шаблону,
  у який залежно від введення підставляється слово "парне" або "непарне".
*Додаткове необов'язкове завдання: тернарний вираз вміє крім визначення парне/непарне так само визначати нуль.
"""

number = input("Введіть число: ")
if number.isdigit():
    number = int(number)
    print(f"Ви ввели {'нуль' if number == 0 else 'парне' if number % 2 == 0 else 'непарне'} число")
else:
    print("не вірне введення")