
empty_tuple = ()
empty_tuple = tuple()
fruits = ('banana', 'orange', 'mango', 'lemon')

#length and accessing elements
print(len(fruits)) # 4 - number of elements
tpl = ('item1', 'item2', 'item3')
first_item = tpl[0]
second_item = tpl[1]

#positive index
first_fruit = fruits[0]
second_fruit = fruits[1]
last_index = len(fruits) -1 
print(first_fruit, second_fruit, last_index)

#negative index
first_fruit = fruits[-4]
second_fruit = fruits[-3]
last_fruit = fruits[-1]
print(first_fruit, second_fruit, last_fruit)

#slicing
all_fruits = fruits[0:4]
print(all_fruits)
all_fruits = fruits[0:]
print(all_fruits)
orange_mango = fruits[1:3] #
print(orange_mango)
orange_to_rest = fruits[1:]
print(orange_to_rest)

#negative slicing
all_fruits = fruits[-4:]
orange_mango = fruits[-3:-1]
orange_to_rest = fruits[-3:]
print(all_fruits)
print(orange_mango)
print(orange_to_rest)

#changing tuples to lists
# fruits[0] = 'kiwi' #gives you a TypeError: 'tuple' object does not support item assignment
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)
fruits = tuple(fruits)
print(fruits)

#item checks
fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits)
print('apple' in fruits)

#joining
vegetables = ('tomato', 'potato', 'cabbage', 'onion', 'carrot')
fruits_veg = fruits + vegetables
print(fruits_veg)

#deletion
del fruits