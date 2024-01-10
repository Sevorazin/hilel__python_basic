from datetime import datetime
from dateutil.relativedelta import relativedelta


def calculate_age(birth_date, death_date):
    today = datetime.now()
    age_difference = relativedelta(
        death_date,
        birth_date
    ) if death_date else relativedelta(
        today,
        birth_date
    )

    years = age_difference.years
    months = age_difference.months
    days = age_difference.days

    return f"{years} років, {months} місяців, {days} днів"


def display_person(person):
    """Отображение данных о человеке в консоли."""
    birth_date_str = person.get('Дата народження', '')
    death_date_str = person.get('Дата смерті', '')

    if death_date_str:
        birth_date = datetime.strptime(birth_date_str, '%Y-%m-%d')
        death_date = datetime.strptime(death_date_str, '%Y-%m-%d')
        age = calculate_age(birth_date, death_date)
    else:
        age = person.get('Вік', '')

    print("""
| {:<15} | {:<15} | {:<15} | {:<15} | {:<15} | {:<15} | {:<31} |
""".format(
        person.get('Ім\'я', '') or '',
        person.get('Прізвище', '') or '',
        person.get('По-батькові', '') or '',
        person.get('Стать', '') or '',
        birth_date_str or '',
        death_date_str or 'Відсутня',
        age or ''
    ))
    print('=' * 143)
