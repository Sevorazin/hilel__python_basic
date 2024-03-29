"""
Наведено список чисел. Порахувати скільки разів трапляється кожне число.
Використовувати функцію підрахунку.
Підказка: для зберігання даних використовувати словник (ключ - саме число,
а значення - скільки разів воно трапляється). Для перевірки знаходження
елемента у словнику використовувати метод get(), або оператор in.
*Додаткові не обов'язкові умови:
- Початковий список розміром 200 елементів формується з чисел
від 1 до 10 включно взятих випадковим чином;
- сформувати підсумковий словник (де ключ це саме число, а значення це
у повторень даного числа в первісному списку) за допомогою
конструкції "генератор словників";
- підсумковий висновок відсортувати по порядку зростання числа, наприклад:
Число 1 зустрічається у первісному списку 10 разів
Число 2 зустрічається у початковому списку 3 рази
Число 3 зустрічається у початковому списку 14 разів
Число 4 зустрічається у початковому списку 1 раз
і т.д.
- використовувати лямбда-функцію для того, щоб визначити яке слово треба
написати для конкретного числа: "раз", "разів" або "раза"
"""

import random
random_list = [random.randint(1, 10) for i in range(200)]
result_dict = {num: random_list.count(num) for num in set(random_list)}
sorted_result = sorted(result_dict.items())
get_word_form = lambda count: "раз" if count % 10 == 1 and count % 100 != 11 else "разів"
for num, count in sorted_result:
    word_form = get_word_form(count)
    print(f"Число {num} зустрічається у первісному списку {count} {word_form}")

