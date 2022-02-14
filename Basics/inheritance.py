class ParentClass:
    def __init__(self):
        print("Parent class instance")

    def parent_method(self):
        print("Parents money")

class childclass(ParentClass):
    pass
# P = ParentClass()
# P.parent_method()
c = childclass()
c.parent_method()
