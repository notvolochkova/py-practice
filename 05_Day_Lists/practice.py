lst = list()

empty_list = list()
print(len(empty_list))

lst = []
empty_list = []
print(len(empty_list))

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'cabbage', 'onion', 'carrot']
animal_products = ['milk', 'meat', 'butter', 'yogurt']
web_tech = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MongoDB']
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

print('Fruits:', fruits)
print('Number of fruits', len(fruits))

print('Vegetables:', vegetables)
print('Number of veg', len(vegetables))

print('Animal products', animal_products)
print('number of animal products', len(animal_products))

print('Web technologies', web_tech)
print('Number of web technologies',len(web_tech))

print('countries:', countries)
print('number of countries', len(countries))

lst = ['Asabeneh', 250, True, {'country':'Finland', 'city':'Helsinki'}]
print(lst)
print(type(lst[2]))

first_fruit = fruits[0]
print(first_fruit)

second_fruit = fruits[1]
print(second_fruit)

#same thing 
last_fruit = fruits[3]
print(last_fruit)
last_index = len(fruits) - 1
last_fruit = fruits[last_index]
print(last_fruit)

first_fruit = fruits[-4]
last_fruit = fruits[-1]
second_last = fruits[-2]
print(first_fruit)
print(last_fruit)
print(second_fruit)

lst = ['item1', 'item2','item3','item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item, second_item, third_item, rest)

fruits = ['banana', 'orange', 'mango', 'lemon', 'lime', 'apple']
first_fruit, second_fruit, third_fruit , *rest = fruits
print(first_fruit, second_fruit, third_fruit, rest)

first, second, third, *rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first, second, third, rest, tenth)

countries = ['Germany', 'France', 'Belgium', 'Sweden', 'Denmark', 'Finland', 'Norway', 'Iceland', 'Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr, fr, bg, sw, scandic, es)

#slicing
# fruits = ['banana', 'orange', 'mango', 'lemon']
# #all these give same results
# all_fruits = fruits[0:4]
# print(fruits)
# print(all_fruits)
# print(fruits[0:])
# print(fruits[::])

# print(fruits[1:3]) 
# print(fruits[1:])
# banana_mango = fruits[::2] #this specifies only step size  (pick every 2nd element)
# print(banana_mango)

#negative indexing
fruits = ['banana','orange','mango', 'lemon']
all_fruits = fruits[-4:]
orange_mango = fruits[-3:-1]
orange_mango_lemon = fruits[-3:]
reverse_fruits = fruits[::-1]
print(fruits)
print(all_fruits)
print(orange_mango)
print(orange_mango_lemon)
print(reverse_fruits)

#modifying lists
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado'
print(fruits)
fruits[1] = 'apple'
print(fruits)
last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits)

#checking
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)
does_exist = 'lime' in fruits
print(does_exist)

#appending at the end
lst = list()
lst.append(first_item)
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)
fruits.append('lime')
print(fruits)

#inserting items
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple')
print(fruits)
fruits.insert(3, 'lime')
print(fruits)

#removing items
fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
fruits.remove('banana')
fruits.remove('lemon')
print(fruits)

#remove via pop
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)
fruits.pop(0)
print(fruits)

#deletion
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[0]
print(fruits)
del fruits[1]
print(fruits)
del fruits[1:3]
print(fruits)
# del fruits
# print(fruits)

#clearing
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)

#copying
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)

#joining or concatenation
positive_numbers = [1,2,3,4,5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print(integers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)

#extend
list1 = ['item1', 'item2']
list2 = ['item3', 'item4', 'item5']
list1.extend(list2)

num1 = [0,1,2,3]
num2 = [4,5,6]
num1.extend(num2)
print('Numbers=',num1)

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers=', negative_numbers)

fruits.extend(vegetables)
print('fruits and vegetables', fruits)


#counting
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))

#index
print(fruits.index('orange'))
print(ages.index(24)) #returns first occurence

#reverse
fruits.reverse()
print(fruits)
ages.reverse()
print(ages)

#sort
fruits = ['lemon', 'orange', 'banana', 'mango']
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)

ages.sort()
print(ages)

ages.sort(reverse=True)
print(ages)







