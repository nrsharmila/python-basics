"""
1. Multiple inheritance - A class can inherit attributes and methods from more than one class.
2. Method Resolution Order (MRO) - Search is done first in current class, then the search continues into parent
classes in depth-first, left-right fashion without searching the same class twice
"""
class MoveCharacter:
    def move_fwd(self):
        print("move fwd 1 step")
    def move_bwd(self):
        print("move bwd 1 step")

class JumpCharacter:
    def jumb_level1(self):
        print("jump character level1")

    def jump_level2(self):
        print("jump character level2")

class Pokeman(MoveCharacter, JumpCharacter):
    pass

# p = Pokeman()
# p.move_fwd()
# p.jump_level2()

class Micky(MoveCharacter, JumpCharacter):
    def move_fwd(self):
        print("move micky")


m = Micky()
m.move_fwd()
print(Micky.mro())
# m.jumb_level1()