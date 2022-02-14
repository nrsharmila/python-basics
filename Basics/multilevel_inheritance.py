

class MoveCharacter:
    def move_fwd(self):
        print("move fwd 1 step")
    def move_bwd(self):
        print("move bwd 1 step")

class JumpCharacter(MoveCharacter):
    def jumb_level1(self):
        print("jump character level1")

    def jump_level2(self):
        print("jump character level2")

class Pokeman(JumpCharacter):
    pass

# p = Pokeman()
# p.move_fwd()
# p.jump_level2()

class Micky(Pokeman):
    def move_fwd(self):
        print("move micky")


m = Micky()
m.move_fwd()
print(Micky.mro())