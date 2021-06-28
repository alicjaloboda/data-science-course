class Student:

    school = 'Online School'

    def __init__(self, firstname, lastname, major):
        self.firstname = firstname
        self.lastname = lastname
        self.major = major

    def fullname_with_major(self):
        return f'{self.firstname} {self.lastname} ma specjalizację ' f'{self.major}!'

    @classmethod
    def set_online_school(cls, new_school):
        cls.school = new_school

    @classmethod
    def split_student(cls, student_str):
        firstname, lastname, major = student_str.split('.')
        return cls(firstname, lastname, major)

class CollegeStudent(Student):
    def __init__(self, firstname, lastname, major,age):
        super().__init__(firstname, lastname, major)
        self.age = age

student_1 = CollegeStudent('Alicja','Nazwisko','Informatyka', 25)
student_2 = Student('Marek','Nazw','IT')
new_student = 'Ala.Lala.Polski'
student_3 = Student.split_student(new_student)

print(student_1.fullname_with_major())
print(student_2.fullname_with_major())
print(student_3.fullname_with_major())