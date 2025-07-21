import sqlite3
import json
import os
from person import Person


class PeopleDatabase:
    def __init__(self, db_name="people.db"):
        self.db_name = db_name
        self.initialize_db()

    def initialize_db(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS people (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT,
            middle_name TEXT,
            birth_date TEXT,
            death_date TEXT,
            gender TEXT
        )
        """)

        conn.commit()
        conn.close()

    def add_person(self, person):
        if not isinstance(person, Person):
            raise ValueError("Must provide a valid Person object")

        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute(
            """
        INSERT INTO people (first_name, last_name, middle_name, birth_date, death_date, gender)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
            (
                person.first_name,
                person.last_name,
                person.middle_name,
                person.birth_date.strftime("%d.%m.%Y") if person.birth_date else None,
                person.death_date.strftime("%d.%m.%Y") if person.death_date else None,
                person.gender,
            ),
        )

        conn.commit()
        conn.close()

    def search_people(self, search_term):
        if not search_term:
            return []

        search_pattern = f"%{search_term}%"

        conn = sqlite3.connect(self.db_name)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute(
            """
        SELECT * FROM people 
        WHERE first_name LIKE ? COLLATE NOCASE
        OR last_name LIKE ? COLLATE NOCASE
        OR middle_name LIKE ? COLLATE NOCASE
        """,
            (search_pattern, search_pattern, search_pattern),
        )

        results = cursor.fetchall()
        people_with_ids = []

        for row in results:
            person = Person(
                first_name=row["first_name"],
                last_name=row["last_name"],
                middle_name=row["middle_name"],
                birth_date=row["birth_date"],
                death_date=row["death_date"],
                gender=row["gender"],
            )
            people_with_ids.append((row["id"], person))

        conn.close()
        return people_with_ids

    def get_all_people(self):
        conn = sqlite3.connect(self.db_name)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM people")
        results = cursor.fetchall()
        people_with_ids = []

        for row in results:
            person = Person(
                first_name=row["first_name"],
                last_name=row["last_name"],
                middle_name=row["middle_name"],
                birth_date=row["birth_date"],
                death_date=row["death_date"],
                gender=row["gender"],
            )
            people_with_ids.append((row["id"], person))

        conn.close()
        return people_with_ids

    def export_to_file(self, filename):
        people_with_ids = self.get_all_people()
        data = [person.to_dict() for _, person in people_with_ids]

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        return len(data)

    def import_from_file(self, filename):
        if not os.path.exists(filename):
            raise FileNotFoundError(f"File {filename} not found")

        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)

        count = 0
        for person_data in data:
            try:
                person = Person.from_dict(person_data)
                self.add_person(person)
                count += 1
            except Exception as e:
                print(f"Error importing person: {e}")

        return count

    def delete_person(self, person_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute("DELETE FROM people WHERE id = ?", (person_id,))
        deleted = cursor.rowcount > 0
        conn.commit()
        conn.close()

        return deleted

    def clear_database(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM people")
        count = cursor.rowcount
        conn.commit()
        conn.close()

        return count

    def count_people(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM people")
        count = cursor.fetchone()[0]

        conn.close()
        return count
