class GroupIsFullException(Exception):
    pass


class Group:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.max_students = 10

    def add_student(self, student):
        if len(self.students) >= self.max_students:
            raise GroupIsFullException(f"Group {self.name} is full!")
        self.students.append(student)

    def delete_student(self, last_name):
        for student in self.students:
            if student.last_name == last_name:
                self.students.remove(student)
                return True
        return False

    def find_student(self, last_name):
        for student in self.students:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        return f"Group {self.name}:\n" + "\n".join(str(s) for s in self.students)
