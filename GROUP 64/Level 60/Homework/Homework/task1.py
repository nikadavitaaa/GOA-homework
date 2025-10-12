class Student:
    student_count = 0

    def __init__(self, student_id, grade):
        # Private ატრიბუტი: __id, მას პირდაპირ კლასის გარედან ვერ მივწვდებით
        self.__id = student_id  

        # Protected ატრიბუტი: _grade, გამოიყენება ატრიბუტისთვის, რომელიც უნდა იყოს ხელმისაწვდომი მხოლოდ კლასში ან მის შვილობილ კლასებში
        self._grade = grade

        Student.student_count += 1

    @classmethod
    def get_student_count(cls):
        return cls.student_count

    def get_id(self):
        return self.__id