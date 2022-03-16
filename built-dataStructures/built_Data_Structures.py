

# What is a List?

heights = [61, 70, 67, 64]

#broken_heights = [65 71 59 62]

heights = [61, 70, 67, 64, 65]

broken_heights = [65, 71, 59, 62]

ints_and_strings = [1, 2, 3, "four", "five", "ints_and_strings"]


sam_height_and_testscore = ["Sam" ,67, 85.5 , True]


#Growing a List: Plus (+)


items_sold = ["cake", "cookie", "bread"]


items_sold_new = items_sold + ["biscuit", "tart"]
print(items_sold_new)


orders = ["daisy", "buttercup", "snapdragon", "gardenia", "lily"]

# Create new orders here:



broken_prices = [5, 3, 4, 5, 4] + [4]



new_orders = ["lilac", "iris"]

orders_combined = orders + new_orders


shopping_line = ["Cole", "Kip", "Chris", "Sylvana"]

shopping_line.remove("Chris")
 
print(shopping_line)

# Your code below: 

order_list = ["Celery", "Orange Juice", "Orange", "Flatbread"]

print(order_list)


order_list.remove("Flatbread")

print(order_list)

new_store_order_list  = ["Orange", "Apple", "Mango", "Broccoli", "Mango"]


print(new_store_order_list)


new_store_order_list.remove("Mango")
print(new_store_order_list)


new_store_order_list.remove("Onions")


class_name_test = [["Jenny"	,90],["Alexus"	,85.5],
["Sam",	83],["Ellie",	101.5]]


print(class_name_test)

sams_score = class_name_test[2][1]
print(sams_score)

ellies_score = class_name_test[-1][-1]
print(ellies_score)

incoming_class = [["Kenny",	"American",	9],
["Tanya",	"Russian",	9],
["Madison"	,"Indian",	7]]

print(incoming_class)

incoming_class[2][2] = 8

print(incoming_class)

incoming_class[-3][-3] = "Ken"

print(incoming_class)


# Your code below: 

first_names = ['Ainsley',
'Ben',
'Chani',
'Depak']

preferred_size = ["Small", "Large", "Medium"]

preferred_size.append("Medium")

print(preferred_size)



customer_data = [["Ainsley"	,"Small"	,True],
["Ben",	"Large",	False],
["Chani","Medium",	True],
["Depak",	"Medium",	False]]


print(customer_data)


customer_data[-2][-1] = False

print(customer_data)

customer_data_final  = customer_data + [["Amit", "Large", True], ["Karim", "X-Large", False]]


customer_data[1].remove(False)

print(customer_data)


print(customer_data_final)

last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 

subjects = ["physics",
"calculus",
"poetry",
"history"]



grades = [9,
97,
8,
88]

gradebook = [["physics",	98],
["calculus",	97],
["poetry"	,8],
["history",	88]]

# print(gradebook)

gradebook.append(["computer science", 100])

gradebook.append(["visual arts", 93])
gradebook[-1][-1] = 98

print(gradebook[-1][-1])

print(gradebook[2].remove(85))


gradebook[3].append('Pass')


print(gradebook)


last_semester_gradebook =[ ["Last Yea"]]

full_gradebook = gradebook + last_semester_gradebook


print(full_gradebook)


# Adding by Index: Insert

front_display_list = ["Mang", "File Mignon", "Chocolate Milk"]
print(front_display_list)

# Your code below: 

store_line = ["Karla", "Maxium", "Martim", "Isabella"]


data_science_topics = ["Machine Learning", "SQL", "Pandas", "Algorithms", "Statistics", "Python 3"]
print(data_science_topics)

# Your code below: 

data_science_topics.pop()

print(data_science_topics)

data_science_topics.pop(2)

print(data_science_topics)



