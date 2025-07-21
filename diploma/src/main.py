import sys
from database import PeopleDatabase
from ui_removing_functions import delete_person, clear_database
from ui_functions import clear_screen, print_menu
from ui_inserting_functions import input_person_data, export_to_file, import_from_file
from ui_searching_functions import search_people, show_all_people


def main():
    db = PeopleDatabase()

    print(f"База даних ініціалізована. Знайдено {db.count_people()} записів.")

    while True:
        choice = print_menu()

        if choice == "1":
            person = input_person_data()
            if person:
                db.add_person(person)
                print(f"Додано новий запис про людину: {person}")

        elif choice == "2":
            search_people(db)

        elif choice == "3":
            show_all_people(db)

        elif choice == "4":
            delete_person(db)

        elif choice == "5":
            clear_database(db)

        elif choice == "6":
            export_to_file(db)

        elif choice == "7":
            import_from_file(db)

        elif choice == "8":
            print("\nДо побачення!")
            sys.exit(0)

        else:
            print("\nНеправильний вибір! Будь ласка, виберіть опцію від 1 до 8.")

        input("\nНатисніть Enter, щоб продовжити...")
        clear_screen()


if __name__ == "__main__":
    main()
