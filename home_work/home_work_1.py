"""
Написати програму використовуючи функції input() та print().
Програма вимагає ввести довільну строку.
Потім необхідно створити 2 строкові змінні,
перша з яких складається лише з парних символів введеної строки,
а друга складається з введеної строки, написаної у зворотній послідовності,
при цьому всі літери повинні бути написані у верхньому регістрі.
Як результат вивести введену строку та дві нові строки,
що вийшли, кожну з нового рядка.
"""

inp_str = input("Введіть довільну строку:")
print(inp_str)
paired_symbols = inp_str[0::2]
print(paired_symbols)
reverse_str = inp_str[::-1]
print(reverse_str.upper())  # усі літери великі зробити
