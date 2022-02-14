class Arearect:
    def __init__(self, l, b):
        self.l = l
        self.b = b


 # class - keyword; arearect - class name;
# we need to  instanciate the variables the init method.whenever you are creating the object need to call init method.
#init method takes self arguments.this reference to the objects.
    #self parameters passed in the methods.calculate (custom methods).
    def calculate_area(self):
        return self.l * self.b

area = Arearect(5, 8)
#area(reference the variable) is hold the objects .
area1 = Arearect(76, 24)
print(area.calculate_area())
print(area1.calculate_area())
