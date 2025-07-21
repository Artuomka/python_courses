def search_people(db):
    search_term = input(
        "\nВведіть пошуковий запит (ім'я, прізвище або по-батькові): "
    ).strip()

    if not search_term:
        print("Пошуковий запит не може бути порожнім!")
        return

    results = db.search_people(search_term)

    if not results:
        print(f"За запитом '{search_term}' нікого не знайдено")
        return

    print(f"\nЗнайдено {len(results)} записів за запитом '{search_term}':")
    for i, (person_id, person) in enumerate(results, 1):
        print(f"{i}. [{person_id}] {person}")


def show_all_people(db):
    people_with_ids = db.get_all_people()

    if not people_with_ids:
        print("\nБаза даних порожня.")
        return

    print(f"\nУсього {len(people_with_ids)} записів в базі даних:")
    for i, (person_id, person) in enumerate(people_with_ids, 1):
        print(f"{i}. [{person_id}] {person}")
