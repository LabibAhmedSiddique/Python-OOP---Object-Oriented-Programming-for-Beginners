class student:
    def __init__(self, student_id, name, age, gpa):
        self.student_id = student_id
        self.name = name
        self._age = age
        self.gpa = gpa


student_nora = student('3211', 'your mom', 15, 3.40)


class backpack:
    def __init__(self):
        self._items = []
