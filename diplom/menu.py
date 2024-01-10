from add_person_to_database import add_person_to_database
from search_for_a_person import search_for_a_person
from main_menu import main_menu
from display_all_people import display_all_people
from delete_person import delete_person

main_menu()

while True:
    print("Меню:")
    print("1. Додати 'Людину' до списку")
    print("2. Пошук 'Людини'")
    print("3. Показати всіх людей")
    print("4. Видалити людину")
    print("5. Вихід")

    choice = input("Виберіть опцію: ")

    if choice == '1':
        add_person_to_database()
    elif choice == '2':
        search_for_a_person()
    elif choice == '3':
        display_all_people()
    elif choice == '4':
        delete_person()
    elif choice == '5':
        print("До побачення!")
        break
    else:
        print("Невірний вибір. Будь ласка, введіть 1, 2, 3, 4, або 5.")

if __name__ == "__main__":
    main_menu()
