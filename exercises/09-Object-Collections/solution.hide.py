class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, person):
        self.students.append(person)

    def remove_student_by_name(self, name):
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                return True
        return False

    def find_student_by_name(self, name):
        for student in self.students:
            if student.name == name:
                return student
        return None


    def total_students(self):
        return len(self.students)

bootcamp = Classroom()