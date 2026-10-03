# # example
# try:
#     print(10 + '5')
# except: 
#     print('Something went wrong')

# # example
# try: 
#     name = input('Enter your name:')
#     year_born = input('Year you were born:')
#     age = 2019 - year_born
#     print(f"You are {name}. And your age is {age}.")
# except:
#     print('Something went wrong')

# # example 
# try:
#     name = input('Enter your name:')
#     year_born = input('Year you were born:')
#     age = 2019 - year_born
#     print(f'You are {name}. And your age is {age}.')
# except TypeError:
#     print(f'Type Error occurred, {type(name)}, {type(year_born)}')
# except ValueError:
#     print('Value Error occurred')
# except ZeroDivisionError:
#     print('Zero Divison Error occurred')

# # example
# try: 
#     name = input('Enter your name:')
#     year_born = input('Year you born:')
#     age = 2026 - int(year_born)
#     print(f'You are {name}. And your age is {age}.')
# except TypeError:
#     print(f'Typer error occurred')
# except ValueError:
#     print('Value error occurred')
# except ZeroDivisionError:
#     print('zero division error occurred')
# else:
#     print('I usually run with the try block')
# finally:
#     print('I always run')

# example
# try:
#     name = input('Enter your name:')
#     year_born = input('Year you born:')
#     age = 2012 - int(year_born)
#     print(f'You are {name}. And your age is {age}.')
# except Exception as e:
#     print(e)

# # unpacking example
# def sum_of_five_nums(a,b,c,d,e):
#     return a + b + c + d + e
# lst = [1,2,3,4,5]
# print(sum_of_five_nums(*lst)) 

# # unpacking in range example
# numbers = range(2,7)
# print(list(numbers))
# args = [2, 7]
# numbers = range(*args)
# print(numbers)

#list or tuple unpack example
# countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
# fin, sw, nor, *rest = countries
# print(fin, sw, nor, rest)
# numbers = [1,2,3,4,5,6,7]
# one, *middle, last = numbers
# print(one, middle, last)

# # unpacking dictionary example
# def unpacking_person_info(name, country, city, age):
#     return f'{name} lives in {country}, {city}. He is {age} year old.'
# dct = {'name':'Asabeneh', 'country':'Finland', 'city':'Helsinki', 'age':250}
# print(unpacking_person_info(**dct))

# # packing example, packing lists
# def sum_all(*args): 
#     s = 0 
#     for i in args: #type tuple
#         s += i
#     return s

# print(sum_all(1,2,3))
# print(sum_all(1,2,3,4,5,6,7))

# # packing dictionaries
# def packing_person_info(**kwargs):
#     for key in kwargs: #type dict
#         print(f"{key} = {kwargs[key]}")
#     return kwargs

# print(packing_person_info(name='Asabeneh',
#                           country='Finland',
#                           city='Helsinki',
#                           age=250))

#spreading in python
lst_one = [1,2,3]
lst_two = [4,5,6,7]
lst = [0, *lst_one, *lst_two]
print(lst)

country_lst_one = ['Finland', 'Sweden', 'Norway']
country_lst_two = ['Denmark', 'Iceland']
nordic_countries = [*country_lst_one, *country_lst_two]
print(nordic_countries)

#enumerate example
for index, item in enumerate([20,30,40]):
    print(index, item)

countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
for index, i in enumerate(countries):
    if i == 'Finland':
        print(f"The country {i} has been found at index {index}")

#zip example
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit':f, 'veg':v})
print(fruits_and_veges)