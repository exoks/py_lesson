from BaseClass import Person

class Student(Person):

    def __init__(self, first_name, last_name, email):
        super(Student, self).__init__(first_name, last_name)
        self.email = email

    def introduce(self):
        print("fist_name: ", self.first_name)
        print("last_name: ", self.last_name)
        print("email : ", self.email)
