from datetime import datetime
from display_utils import calculate_age


class Person:
    def __init__(
            self,
            name,
            date_of_birth,
            sex,
            surname=None,
            patronymic=None,
            date_of_death=None
    ):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.sex = sex
        self.date_of_birth = datetime.strptime(
            date_of_birth,
            '%d.%m.%Y'
        ) if date_of_birth else None
        self.date_of_death = (
            datetime.strptime(
                date_of_death,
                '%d.%m.%Y'
            ) if date_of_death else None
        )
        self.age = calculate_age(self.date_of_birth, self.date_of_death)
