# break: Breaks out from the nearest enclosing loop
# continue: Go to the start of nearest enclosing loop
#
# while <expression>:
#     <statement(s)>
#     break
#     <statement(s)>
#     continue
#     <statement(s)>
#     <statement(s)>
# else clause:
#     while <expression>:
#         <statement(s)>
#     else:
#         <statement(s)>

# x = 0
# while x <= 10:
#     print(x)
#     x = x + 1
#     continue
#     print("inside while")
#
# print("out of while loop")

# x = 0
# y = 0
# while x <= 10:
#     print(x)
#     x = x + 1
#     print("parent while")
#     while y < 5:
#         print(y)
#         break
#         print("inside while")
#     print("out of while loop")

# x = 0
# y = 0
# while x <= 10:
#     print(x)
#     x = x + 1
#     print("parent while")
#     while y < 5:
#         print(y)
#         y = y + 1
#         continue
#         print("inside while")
#     print("out of while loop")

x = 0
while x <= 10:
    print(x)
    x = x + 1
    if x == 5:
        break
else:
    print("out of while loop")