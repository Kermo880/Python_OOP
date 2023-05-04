class Student:
    def __init__(self, name, school, assignments_completed=0):
        self.__name = name
        self.__school = school
        self.__assignments_completed = assignments_completed
        self.__laziness = "true" if self.__assignments_completed == 0 else "false"
    
    def is_homework_done(self):
        return self.__assignments_completed >= 1
    
    def get_school(self):
        return self.__school
    
    def get_name(self):
        return self.__name
    
    def get_laziness(self):
        return self.__laziness
    
    def change_school(self, new_school):
        self.__school = new_school
    
    def complete_assignment(self):
        self.__assignments_completed += 1
        self.__laziness = "false"
        
    def get_attendance(self):
        return self.__attendance_record
    
student = Student("John Doe", "Random School")
print(student.get_name())
print(student.get_school())
print(student.get_laziness())

# student.complete_assignment()
# print(student.get_laziness())