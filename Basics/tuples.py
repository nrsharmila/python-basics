# tuples are indexed, allow duplicate values and cannot be modified(immutable)
demo_tuple = (10, 20, 30, 40)
demo_tuple1 = ("Madurai", "Madurai", "Bangalore", "Chennai", "Mumbai")
demo_tuple2 = (True, False, False, True)
demo_tuple3 = (True, 0, "Madurai", 20.3)
print(demo_tuple1[1])
print(len(demo_tuple))
print(type(demo_tuple1))
print(demo_tuple1.count("Madurai"))
print(demo_tuple1.index("Bangalore"))

for x in demo_tuple1:
    print(x)

    joined_tuple = demo_tuple3 + demo_tuple2 + demo_tuple
    print(joined_tuple)

#joined_tuple = demo_tuple + demo_tuple1
# print(joined_tuple)
