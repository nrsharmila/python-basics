demo_dict = {'QA': 'Qaurl', 'uat': 'uaturl', 'prod': 'produrl', 1: 56}

# get() - Returns the value for specified key in the dictionary
print(demo_dict.get('prod'))

# keys() - Returns a copy of dictionary's keys
print(demo_dict.keys())

# items() - Returns a copy for dictionaries key:value pair.
print(demo_dict.items())

# values() - Returns a copy of the values in the dictionary.
print(demo_dict.values())

#  pop() - Removes the items with the specified key
print(demo_dict.pop(1))

# popitem() - Removes the arbitrary key:value pair
print(demo_dict.popitem())

# update() - Add the specified key:value pairs in dictionary
demo_dict.update({'qa': 3})
print(demo_dict)

# copy() - Returns a copy of the dictionary
demo_dict1 = demo_dict.copy()
print(demo_dict1)

# clear() - Removes all the elements from the dictionary
print(demo_dict1.clear())