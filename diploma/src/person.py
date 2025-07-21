from datetime import datetime
import re


class Person:
    def __init__(
        self,
        first_name,
        last_name=None,
        middle_name=None,
        birth_date=None,
        death_date=None,
        gender=None,
    ):
        if not first_name:
            raise ValueError("First name is required")

        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.birth_date = self._parse_date(birth_date) if birth_date else None
        self.death_date = self._parse_date(death_date) if death_date else None
        self.gender = gender.lower() if gender else None

        if self.birth_date and self.death_date and self.birth_date > self.death_date:
            raise ValueError("Birth date cannot be after death date")

    def _parse_date(self, date_str):
        date_str = date_str.strip()
        # DD.MM.YYYY, DD-MM-YYYY, DD/MM/YYYY, DD MM YYYY
        formats = [
            r"(\d{1,2})[.\-/ ](\d{1,2})[.\-/ ](\d{4})",
        ]

        for fmt in formats:
            match = re.match(fmt, date_str)
            if match:
                day, month, year = map(int, match.groups())
                try:
                    return datetime(year, month, day)
                except ValueError:
                    continue

        raise ValueError(f"Invalid date format: {date_str}")

    def get_age(self, reference_date=None):
        if not self.birth_date:
            return None

        end_date = (
            self.death_date if self.death_date else (reference_date or datetime.now())
        )

        age = end_date.year - self.birth_date.year

        if (end_date.month, end_date.day) < (
            self.birth_date.month,
            self.birth_date.day,
        ):
            age -= 1

        return age

    def get_full_name(self):
        parts = []
        if self.first_name:
            parts.append(self.first_name)
        if self.last_name:
            parts.append(self.last_name)
        if self.middle_name:
            parts.append(self.middle_name)
        return " ".join(parts)

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "middle_name": self.middle_name,
            "birth_date": self.birth_date.strftime("%d.%m.%Y")
            if self.birth_date
            else None,
            "death_date": self.death_date.strftime("%d.%m.%Y")
            if self.death_date
            else None,
            "gender": self.gender,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            first_name=data["first_name"],
            last_name=data["last_name"],
            middle_name=data["middle_name"],
            birth_date=data["birth_date"],
            death_date=data["death_date"],
            gender=data["gender"],
        )

    def __str__(self):
        age = self.get_age()
        age_str = f"{age} {'років' if age in [0, 5, 6, 7, 8, 9] or age > 10 else 'рік' if age == 1 else 'роки'}"
        gender_text = (
            "чоловік"
            if self.gender == "m"
            else "жінка"
            if self.gender == "f"
            else "невідома стать"
        )
        name = self.get_full_name()

        birth_str = (
            f"Народи{'в' if self.gender == 'm' else 'ла' if self.gender == 'f' else 'в/ла'}ся {self.birth_date.strftime('%d.%m.%Y')}"
            if self.birth_date
            else "Дата народження невідома"
        )

        death_str = (
            f"{'Помер' if self.gender == 'm' else 'Вмерла' if self.gender == 'f' else 'Помер/ла'}: {self.death_date.strftime('%d.%m.%Y')}"
            if self.death_date
            else ""
        )

        result = f"{name} {age_str}, {gender_text}. {birth_str}."
        if death_str:
            result += f" {death_str}."

        return result
