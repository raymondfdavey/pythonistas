class Student:
    """A class to represent a University student."""
    def __init__(self, firstname, lastname, course):
        self.firstname=firstname
        self.lastname=lastname
        self.course=course
        self.modules = []

    def add_module(self, module_code):
        self.modules.append(module_code)
        
    def show_details(self):
        print(f"{self.firstname} {self.lastname} studying {self.course}")
        print("enrolled on following modules:")
        for module in self.modules:
            print(module)
    def change_course(self, new_course):
        print(f"{self.firstname} {self.lastname} course changed from {self.course} to {new_course}")
        self.course = new_course
        
class Module:
    """A class to represent a single module."""
    def __init__(self, module_name, module_code, module_teacher):
        self.name=module_name
        self.code=module_code
        self.teacher=module_teacher
        self.enrolled_students = []
        
    def enrol_student(self, student_object):
        student_object.add_module(self.code)
        self.enrolled_students.append(student_object)
    
    def show_all_enrolled_students(self):
        print(f"students enrolled in module {self.name} are:")
        for student_object in self.enrolled_students:
            print(f"{student_object.firstname} {student_object.lastname}")


def main():

    # Create some students and some modules...
    s1 = Student('Ken', 'Barlow', 'English')
    s2 = Student('Mike', 'Baldwin', 'Business')
    s3 = Student('Harold', 'Legg', 'Medicine')

    m1 = Module('English language and semantics', 'A101', 'Wanda Pickle')
    m2 = Module('Engineering principles', 'E102', 'Buzz Jones')
    m3 = Module('Anatomy', 'M105', 'Greg House')

    # Now enrol some students on some modules...
    m1.enrol_student(s1)
    m1.enrol_student(s2)
    m2.enrol_student(s1)
    m2.enrol_student(s3)

    # Have a look at some students and some modules...
    s1.show_details()
    s2.show_details()
    s3.show_details()

    m1.show_all_enrolled_students()
    m2.show_all_enrolled_students()
    m3.show_all_enrolled_students()

    # Change a course...
    s1.change_course('Engineering')
    s1.show_details()


if __name__ == "__main__":
    main()
