# used to iterate over the sequence like list, string, dictionary, set or tuple
# less like the for loop in other programming language.

# city = "Delhi"
# for c in city:
#     print(c)

# city = ("Delhi", "Melbourne", "Bangalore", "Chennai")
# for c in city:
#     print(c)

# city = (["Delhi","Hindi"],["Melbourne", "Bangalore"],["Chennai","madurai"])
# for c in city:
#     print(c)

cities = (["Delhi","Hindi"],["Melbourne", "Bangalore"],["Chennai","madurai"])
# for country,city in cities:
#     print("country is" +country+ "and city is" +city)

my_dict = dict(cities)
print(my_dict)
for country, city in my_dict.items():
    print(country,city)