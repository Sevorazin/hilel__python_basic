"""
Прочитати збережений json-файл з попереднього завдання та записати дані на диск у csv-файл, першим стовпцьом буде ID
 (6-ти значне число, котре у попередньому завданні було ключем) і додавши новий стовпець "телефон". Крім цього,
  необхідно для кожного запису додати значення нової комірки “телефон”.
Значення має бути заповнене випадковими цифрами.
Назви стовпців будуть наступні:
ID,
 Ім'я,
  Вік,
   Телефон.
При цьому значення для перших трьох комірок необхідно дістати з json-файлу для кожного запису,
 а значення нової комірки "Телефон" сформувати.
*Додаткове завдання не обов'язкове до виконання.
Формування значення комірки телефону має бути наступним:
• не всі люди можуть мати номер телефону. Хто має номер телефону, а хто ні визначається автоматично випадковим чином.
 З ймовірністю 75% осіб має номер телефону, з ймовірністю 25% - ні;
• є список можливих трьох перших цифр (операторів), Наприклад: ['095', '066', '098', '096', '050', '097']
• при формуванні нового номера телефону перші 3 цифри вибираються випадковим чином зі списку можливих операторів,
 решта 7 цифр може бути будь-якими і формуються випадковим чином.
Для виконання цього завдання необхідно розібратися з бібліотекою "random"
"""

import json
import csv
import random

json_file_path = r'D:\python_project\hilel_python_basic\lesson_11\home_work_18\data.json'
with open(json_file_path, 'r') as json_file:
    data = json.load(json_file)


def generate_phone_number():
    operators = ['095', '066', '098', '096', '050', '097']
    has_phone = random.random() < 0.75
    if has_phone:
        return f'{random.choice(operators)}{random.randint(1000000, 9999999)}'
    else:
        return ''



csv_file_path = 'output_data.csv'
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ['ID', 'Ім\'я', 'Вік', 'Телефон']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()

    for key, value in data.items():
        id_number = key
        name = value[0]
        age = value[1]
        phone_number = generate_phone_number()

        writer.writerow({'ID': id_number, 'Ім\'я': name, 'Вік': age, 'Телефон': phone_number})

print(f"Дані були успішно записані у файл '{csv_file_path}'")
