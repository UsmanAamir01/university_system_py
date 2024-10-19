
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Human):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id


class Teacher(Human):
    def __init__(self, name, age, teacher_id):
        super().__init__(name, age)
        self.teacher_id = teacher_id


class Section:
    def __init__(self, section_name, no_of_sections, timings):
        self.section_name = section_name
        self.no_of_sections = no_of_sections
        self.timings = timings
        self.students = []
        self.teachers = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)


class University:
    def __init__(self, university_name):
        self.university_name = university_name
        self.students = []
        self.teachers = []
        self.sections = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_section(self, section):
        self.sections.append(section)

    def display_details(self):
        print(f"\nUniversity: {self.university_name} \n")

        print("Students:")
        for student in self.students:
            print(
                f" - {student.name}, Age: {student.age}, ID: {student.student_id}")

        print("\nTeachers:")
        for teacher in self.teachers:
            print(
                f" - {teacher.name}, Age: {teacher.age}, ID: {teacher.teacher_id}")

        print("\nSections:")
        for section in self.sections:
            print(f" - {section.section_name}, No. of Sections: {
                  section.no_of_sections}, Timings: {section.timings}")
            print("   Students Enrolled:")
            for student in section.students:
                print(f"     * {student.name}, ID: {student.student_id}")
            print("   Teachers Assigned:")
            for teacher in section.teachers:
                print(f"     * {teacher.name}, ID: {teacher.teacher_id}")


university = University("FAST NUCES CFD CAMPUS")


std1 = Student("Usman Aamir", 20, 101)
std2 = Student("Ruman Aamir", 19, 102)

t1 = Teacher("Mansoor Ali", 30, 1001)
t2 = Teacher("Minahil Azeem", 29, 1002)

sec = Section("BSE-5B", 4, "9:00 AM - 11:00 AM")
university.add_student(std1)
university.add_student(std2)

university.add_teacher(t1)
university.add_teacher(t2)

university.add_section(sec)


sec.add_student(std1)
sec.add_student(std2)
sec.add_teacher(t1)
sec.add_teacher(t2)

university.display_details()
