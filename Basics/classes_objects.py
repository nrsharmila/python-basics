class Employee:
    def __init__(self, fname, lname, email):
        self.fname = fname
        self.lname = lname
        self.email = email


    def greet_person(self):
        print("Hello, Welcome to the Google" + self.fname)



emp1 = Employee('Sharmila', 'Ravindran', 'nsseeshar@gmail.com')
emp2 = Employee('Manish', 'verma', 'manish@gmail.com')
print(emp1.fname)
print(emp2.fname)

emp1.greet_person()



