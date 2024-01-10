import openpyxl
from class_person import Person
from datetime import datetime


def add_person_to_database():
    while True:
        name = input("Введіть ім'я: ")
        if name.strip():
            break
        else:
            print("Ім'я не може бути порожнім. Спробуйте знову.")

    surname = input("Введіть прізвище (необов'язково): ")
    patronymic = input("Введіть по-батькові (необов'язково): ")

    print("Виберіть стать (необов'язково):")
    print("1. Чоловіча")
    print("2. Жіноча")
    gender_choice = input("Ваш вибір: ")

    if gender_choice == '1':
        sex = 'Чоловіча'
    elif gender_choice == '2':
        sex = 'Жіноча'
    else:
        print("Невірний вибір. Вибрано значення за замовчуванням: Приховано.")
        sex = 'Приховано'

    while True:
        date_of_birth = input("Введіть дату народження (формат: dd.mm.yyyy): ")
        try:
            if date_of_birth:
                birth_date = datetime.strptime(date_of_birth, '%d.%m.%Y')

                if birth_date <= datetime.now():
                    break
                else:
                    print("Дата народження не може бути у майбутньому.")
            else:
                print("Дата народження обов'язково повинна бути.")
        except ValueError:
            print("Невірний формат дати. Спробуйте ще раз.")

    person = Person(name, date_of_birth, sex, surname, patronymic, None)

    while True:
        date_of_death = input(
            "Введіть дату смерті (необов'язково), формат: dd.mm.yyyy): "
        )
        if not date_of_death:
            person.date_of_death = None
            break

        try:
            death_date = datetime.strptime(date_of_death, '%d.%m.%Y')
            if person.date_of_birth and death_date < person.date_of_birth:
                print("Дата смерті не може бути раніше дати народження.")
            else:
                person.date_of_death = death_date
                break
        except ValueError:
            print("Невірний формат дати смерті. Спробуйте ще раз.")

    wb = openpyxl.load_workbook('database.xlsx')
    ws = wb.active

    row_data = [person.name, person.surname, person.patronymic, person.sex,
                person.date_of_birth.strftime('%Y-%m-%d'),
                person.date_of_death.strftime(
                    '%Y-%m-%d'
                ) if person.date_of_death
                else None,
                person.age]

    ws.append(row_data)

    wb.save('database.xlsx')
    print("Людина додана до бази даних.")


if __name__ == "__main__":
    add_person_to_database()
