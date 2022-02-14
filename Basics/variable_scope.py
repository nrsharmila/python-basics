# Variable scope in python - boundary of variables within a program
# Local scope
# Global scope
# global keyword
# LEGB rule - local -> elclosing -> global -> build-in
#x = 20 (global scope of variable includes for all functions)
# def var_scope_demo():
#     # x = 20 (Local scope defining within particular function)
#     global x
#     x = 20
#     print(x)
#
# def var_scope_demo1():
#     print(x)
#
# var_scope_demo()
# var_scope_demo1()

#LEGB rule
#Parent
def var_scope_demo():
     x = 20
     print(x)
     #child
     def var_scope_demo1():
          print(x)
          #enclosing
          def grand_child():
              print(x)
          grand_child()
     var_scope_demo1()

var_scope_demo()






