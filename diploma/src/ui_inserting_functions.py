from person import Person


def input_person_data():
    print("\n----- Введіть дані про людину -----")

    while True:
        first_name = input("Ім'я (обов'язково): ").strip()
        if first_name:
            break
        print("Ім'я є обов'язковим полем!")

    last_name = input("Прізвище (опціонально): ").strip() or None
    middle_name = input("По-батькові (опціонально): ").strip() or None

    while True:
        birth_date = (
            input("Дата народження (DD.MM.YYYY, опціонально): ").strip() or None
        )
        if not birth_date or is_valid_date_format(birth_date):
            break
        print(
            "Неправильний формат дати! Використовуйте DD.MM.YYYY, DD-MM-YYYY, DD/MM/YYYY або DD MM YYYY"
        )

    while True:
        death_date = input("Дата смерті (DD.MM.YYYY, опціонально): ").strip() or None
        if not death_date or is_valid_date_format(death_date):
            break
        print(
            "Неправильний формат дати! Використовуйте DD.MM.YYYY, DD-MM-YYYY, DD/MM/YYYY або DD MM YYYY"
        )

    while True:
        gender = input("Стать (m/f, опціонально): ").strip().lower() or None
        if not gender or gender in ["m", "f"]:
            break
        print("Стать має бути 'm' (чоловіча) або 'f' (жіноча)!")

    try:
        person = Person(
            first_name=first_name,
            last_name=last_name,
            middle_name=middle_name,
            birth_date=birth_date,
            death_date=death_date,
            gender=gender,
        )
        return person
    except ValueError as error:
        print(f"Виникла помилка: {error}")
        return None


def is_valid_date_format(date_str):
    try:
        person = Person(first_name="Temp")
        person._parse_date(date_str)
        return True
    except ValueError:
        return False


def export_to_file(db):
    filename = input(
        "\nВведіть назву файлу для експорту (наприклад, people.json): "
    ).strip()

    if not filename:
        print("Назва файлу не може бути порожня!")
        return

    try:
        count = db.export_to_file(filename)
        print(f"Успішно експортовано {count} записів у файл '{filename}'")
    except Exception as e:
        print(f"Під час експорту виникла помилка: {e}")


def import_from_file(db):
    filename = input("\nВведіть назву файлу для імпорту: ").strip()

    if not filename:
        print("Назва файлу не може бути порожньою!")
        return

    try:
        count = db.import_from_file(filename)
        print(f"Успішно імпортовано {count} записів з файлу '{filename}'")
    except FileNotFoundError:
        print(f"Файл '{filename}' не знайдено!")
    except Exception as e:
        print(f"Помилка під час імпорту: {e}")
