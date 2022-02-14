class RateOfInterest:
# object is created for that particular person is called instance variables.
     def __init__(self, name, loan, interest):
         self.name = name
         self.loan = loan
         self.interest = interest

     def calc_interest(self):
         print("Total interest: ", self.loan * self.interest)



person = RateOfInterest("sharmila", 500000, 0.06)
person.calc_interest()


#outside of the method is created object is called class variable.