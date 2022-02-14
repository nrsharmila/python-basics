list1 = ["India", "USA", "UK", "London"]
list2 = ["Pune", "New york", "Sydney"]
# s = zip(list1,list2)
# print(list(s))
#zip function to iteration multiple lists.
total_cost = [45,67,65,87]
sale_price = [55,77,89,76]
for x,y in zip(total_cost,sale_price):
    print(y-x)