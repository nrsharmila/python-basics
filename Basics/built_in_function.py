# max() Returns the largest item in an iterable
# demo_tuple = (5,7,8,4,1,0)
# x = max(demo_tuple)
# print(x)

# min() Returns the smallest item in an iterable
# demo_tuple = (5,7,8,4,1,0)
# x = min(demo_tuple)
# print(x)

# iter() Returns an iterator object
demo_tuple = (5,7,8,4,3,2)
i = iter(demo_tuple)
print(next(i))
print(next(i))

# reversed() Returns a reversed iterator
demo_tuple = (5,7,8,4,3,2)
j = reversed(demo_tuple)
print(next(j))
print(next(j))

# next() Returns the next item in an iterable

# slice() Returns a slice object
demo_tuple = (5,7,8,4,3,2)
x = slice(2,5)
print(demo_tuple[x])

# Sorted() Returns a sorted list
demo_tuple = (5,7,8,4,3,2)
x = sorted(demo_tuple)
print(x)

# sum() sums the items of iterator
demo_tuple = (5,7,8,4,3,2)
a = sum(demo_tuple)
print(a)

# input() Allows user to input value
y = input("Enter your name:")
print("Welcome "+ y)
