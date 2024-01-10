import os
import openpyxl


def main_menu():
    if not os.path.exists('database.xlsx'):
        wb = openpyxl.Workbook()
        ws = wb.active
        header = [
            "Ім'я",
            "Прізвище",
            "По-батькові",
            "Стать",
            "Дата народження",
            "Дата смерті",
            "Вік"
        ]
        ws.append(header)
        wb.save('database.xlsx')
        print("Створено новий файл 'database.xlsx'.")
