"""
Даний рядок у байтовому вигляді: b'r\xc3\xa9sum\xc3\xa9' закодована в кодуванні за умовчанням utf-8.
Декодувати її у рядковий вигляд у кодуванні за замовчуванням.
Потім результат знову перетворити на байтовий, тільки вже в кодуванні 'Latin1'
І на кінець результат знову декодувати у рядок
(Результати всіх перетворень виводити на екран).
"""


byte_string = b'r\xc3\xa9sum\xc3\xa9'

decoded_string_utf8 = byte_string.decode('utf-8')
print("Декодований рядок в utf-8:", decoded_string_utf8)

byte_string_latin1 = decoded_string_utf8.encode('latin1')
print("Байтовий рядок в Latin1:", byte_string_latin1)

decoded_string_latin1 = byte_string_latin1.decode('latin1')
print("Декодований рядок в Latin1:", decoded_string_latin1)
