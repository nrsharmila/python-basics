#dictionaries are used to store data in key:value pairs.They are changeable and they do not allow the duplicate allows.
#difining dictionaries
demo_dict = {1:20, 2:10, 3:30}
demo_dict1 = {"QA":"Qaurl", "uat":"uaturl"}
demo_dict2 = {'QA': 2, 4:'Url'}

#Accessing items from dictionaries
print(demo_dict[2])
print(demo_dict2['QA'])

#Adding items to dictionaries
demo_dict1['prod'] = 'produrl'
demo_dict1[1] = 56
print(demo_dict1)

#Removing items from dictionaries
demo_dict1.pop(1)
print(demo_dict1)

