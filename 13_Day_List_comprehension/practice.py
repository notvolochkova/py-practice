
#example1
language = 'Python'
lst = list(language)
print(type(lst))
print(lst)

lst = [i for i in language]
print(type(lst))
print(lst)

#example2 - generate list of numbers
numbers = [i for i in range(11)]
print(numbers)

squares = [i * i for i in range(11)]
print(squares)

numbers = [(i, i * i) for i in range(11)]
print(numbers)

#example3 - even numbers
even_numbers = [i for i in range(21) if i % 2 == 0]
print(even_numbers)

odd_numbers = [i for i in range(21) if i % 2 != 0]
print(odd_numbers)

#filtering numbers
numbers = [i for i in range(21)]
positive_even_numbers = [i for i in numbers if i % 2 == 0 and i > 0]
print(positive_even_numbers)

#flattening
list_of_lists = [[1,2,3], [4,5,6], [7,8,9]]
flattened_list = [number for row in list_of_lists for number in row]
print(flattened_list)

#named function
# def add_two_nums(a,b):
#     return a + b
# print(add_two_nums(2,3))

#lambda function
add_two_nums = lambda a, b: a+b
print(add_two_nums(2,3))

#self-invoking lambda
print((lambda a,b: a+b)(2,3))

square = lambda x : x ** 2
print(square(3))

cube = lambda x : x ** 3
print(cube(3))

#multiple variables
multiple_variables = lambda a,b,c: a ** 2 - 3 * b + 4 * c
print(multiple_variables(5,5,3))

#lambda function inside another function
def power(x):
    return lambda n : x ** n
cube = power(2)(3)
print(cube)

two_power_of_five = power(2)(5)
print(two_power_of_five)