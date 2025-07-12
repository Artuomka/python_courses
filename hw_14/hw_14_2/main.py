from classes.student import Student
from classes.group import Group, GroupIsFullException


def main():
    st1 = Student("Male", 30, "Steve", "Jobs", "AN142")
    st2 = Student("Female", 25, "Liza", "Taylor", "AN145")
    gr = Group("PD1")
    gr.add_student(st1)
    gr.add_student(st2)
    print(gr)
    assert gr.find_student("Jobs") == st1, "Test1"
    assert gr.find_student("Jobs2") is None, "Test2"

    gr.delete_student("Taylor")
    print(gr)

    gr.delete_student("Taylor")

    for i in range(10):
        student = Student("Male", 20, f"Name{i}", f"Last{i}", f"RB{i}")
        try:
            gr.add_student(student)
            print(f"Added: {student}")
        except GroupIsFullException as e:
            print(f"Exception caught: {e}")
            break


main()
