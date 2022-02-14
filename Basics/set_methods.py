#add elements
demo_set1 = {10, 20, 30, 40}
print(demo_set1)
demo_set1.add(50)
print(demo_set1)

#remove elements
demo_set2 = {"gold", "diamond", "silver", "ruby", "platinum", 50}
print(demo_set2)
#demo_set2.remove("silver")
#print(demo_set2)

#discard elements
#demo_set2.discard("silver")
#print(demo_set2)

#pop()
#demo_set2.pop()
#print(demo_set2)

#clear()
#demo_set2.clear()
#print(demo_set2)

#Joining two sets
#union()
#update()
#demo_set3 = demo_set1.union(demo_set2)
#print(demo_set3)
#demo_set1.update(demo_set2)
#print(demo_set1)

#keep only duplicates
#intersections()
#intersections_update()
#demo_set3 = demo_set1.intersection(demo_set2)
#print(demo_set3)
#demo_set1.intersection_update(demo_set2)
#print(demo_set1)

#keep all excluding duplicates
#symmetric_difference()
#symmetric_difference_update()
#demo_set3 = demo_set1.symmetric_difference(demo_set2)
#print(demo_set3)
#demo_set1.symmetric_difference_update(demo_set2)
#print(demo_set1)

#Returns set containing difference between two or more sets
#difference()
#difference_update()
#demo_set3 = demo_set1.difference(demo_set2)
#print(demo_set3)
#demo_set2.difference_update(demo_set1)
#print(demo_set2)

#issubset()
#issuperset()
z = demo_set2.issubset(demo_set1)
print(z)
z = demo_set2.issuperset(demo_set1)
print(z)


