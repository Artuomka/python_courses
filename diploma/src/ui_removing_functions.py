def delete_person(db):
    people_with_ids = db.get_all_people()

    if not people_with_ids:
        print("\nБаза даних порожня. Немає записів про людей для видалення.")
        return

    print("\n----- Список людей для видалення -----")
    for i, (person_id, person) in enumerate(people_with_ids, 1):
        print(f"{i}. [{person_id}] {person}")

    while True:
        try:
            selection = input(
                "\nВведіть номер людини для видалення (або 0 для скасування): "
            ).strip()
            if selection == "0":
                print("Операцію скасовано.")
                return

            index = int(selection) - 1
            if 0 <= index < len(people_with_ids):
                break
            else:
                print(f"Будь ласка, введіть число від 1 до {len(people_with_ids)}.")
        except ValueError:
            print("Будь ласка, введіть коректне число.")

    person_id, person = people_with_ids[index]

    confirm = (
        input(f"\nВи впевнені, що хочете видалити '{person}'? (так/ні): ")
        .strip()
        .lower()
    )
    if confirm != "так":
        print("Операцію скасовано.")
        return

    if db.delete_person(person_id):
        print("Людину успішно видалено.")
    else:
        print("Помилка під час видалення.")


def clear_database(db):
    count = db.count_people()

    if count == 0:
        print("\nБаза даних вже порожня.")
        return

    print(f"\nУВАГА: Ви збираєтесь видалити ВСІ {count} записів з бази даних!")
    confirm = input(
        "Ця дія НЕЗВОРОТНА. Введіть 'ВИДАЛИТИ ВСЕ' для підтвердження: "
    ).strip()

    if confirm != "ВИДАЛИТИ ВСЕ":
        print("Операцію скасовано.")
        return

    second_confirm = (
        input("Ви ВПЕВНЕНІ? Введіть 'так' для остаточного підтвердження: ")
        .strip()
        .lower()
    )
    if second_confirm != "так":
        print("Операцію скасовано.")
        return

    deleted_count = db.clear_database()
    print(f"Базу даних очищено. Видалено {deleted_count} записів.")
