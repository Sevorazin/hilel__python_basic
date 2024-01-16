"""
Ввести з клавіатури 4 рядки та зберегти їх у 4 різні змінні.
Створити файл і записати в нього перші 2 рядки та закрити файл.
Потім відкрити файл на редагування і дозаписати 2 рядки, що залишилися.
У підсумку файл має бути 4 рядки, кожен з яких повинен починатися з нового рядка.
"""

row1 = input("Введіть перший рядок: ")
row2 = input("Введіть другий рядок: ")
row3 = input("Введіть третій рядок: ")
row4 = input("Введіть четвертий рядок: ")

with open("myfile.txt", "w") as file:
    file.write(row1 + "\n")
    file.write(row2 + "\n")

with open("myfile.txt", "a") as file:
    file.write(row3 + "\n")
    file.write(row4 + "\n")

with open("myfile.txt", "r") as file:
    content = file.read()
    print("Зміст файлу:")
    print(content)