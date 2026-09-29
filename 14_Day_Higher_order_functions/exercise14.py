

#ex1.1
'''
Explain the difference between map, reduce and filter
map() takes a function and iterables as parameter and executes the function on the iterable.
map() will iterate over the iterable make the changes and return a new iterable

filter() takes function and iterable as parameters, it executes the function which returns a boolean
for each item of the iterable and returns a new iterable which satisfies the conditions of the function (those which are True)

reduce() is from functools, takes function and iterable as parameters, it does not return a new iterable
it will return a single value, hence the name
'''

#ex1.2
'''
Explain the difference between higher order function, closure and decorator

Not all decorators are closures and not all closures are decorators. Both decorators and closures are considered HOF

HOF is an umbrella term in computer science or programming meaning either condition met:
1. A function can take another function as a parameter or argument
2. A function is returned as a value

Decorators denoted by `@decorator_name` above the function definition to decorate/enhance may or may not contain closures,
but it should take the target_function as a parameter, and return the function. It is optional if it has an inner wrapper function.

Closure is nesting functions. There will be an outer enclosing function and an inner function. Closures are also an umbrella term
for programming and computer science, they are not specific to decorators in Python only. One can see if a funciton is a closure by
`func.__closures__` 
'''

#ex1.3

#ex1.4
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [i for i in range(1,11)] 

def printer(target_function):
    def wrapper(*args, **kwargs):
        value = target_function(*args, **kwargs)
        print(f"\'{target_function.__name__}\' invoked print")
        [print(i) for i in args[0]]
        return value
    return wrapper

@printer
def iterate_over_stuff(lst):
    return None

#ex1.4
iterate_over_stuff(countries)
#ex1.5
iterate_over_stuff(names)
#ex1.6
iterate_over_stuff(numbers)

#ex2.1
def upper_iterable(string):
    return string.upper()
new_countries = list(map(upper_iterable, countries))
print(new_countries)

#ex2.2
def square_number(number):
    return number ** 2
new_numbers = list(map(square_number, numbers))
print(new_numbers)

#ex2.3
new_names = list(map(lambda string: string.upper(), names))
print(new_names)

#ex2.4
def is_land(string):
    if 'land' in string:
        return True
    return False

land_countries = list(filter(is_land, countries))
print(land_countries)

#ex2.5
def is_six_chars(string):
    if len(string) == 6:
        return True
    return False
six_char_countries = list(filter(is_six_chars, countries))
print(six_char_countries)

#ex2.6
def is_six_or_more(string):
    if len(string) >= 6:
        return True
    return False
six_and_more_countries = filter(is_six_or_more, countries)
print(list(six_and_more_countries))

#ex2.7
def starts_with_E(string):
    if string.startswith('E'):
        return True
    return False 
E_countries = list(filter(starts_with_E, countries))
print(E_countries)

#ex2.8

#ex2.9
def get_string_lists(item):
    if isinstance(item, str):
        return True
    return False
random_lst = [1,4,'new_string', False, 'brother', 'xxx', 290.3]
filtered_list = list(filter(get_string_lists, random_lst))
print(filtered_list)

#ex2.10
from functools import reduce
total = reduce(lambda i, j: i+j, numbers)
print(total)

#ex2.11
country_statement = reduce(lambda str1, str2:
                            str1 + " and " + str2  + " are north European countries"
                            if str2 == 'Iceland' 
                            else str1 + ", " + str2 , countries)
print(country_statement)

#ex2.12
from pathlib import Path
import sys
parent = Path(__file__).resolve().parent.parent / "data"
sys.path.append(str(parent))

from countries import countries
country_list = countries.copy()

def categorize_countries(lst, pattern):
    return list(filter(lambda country: pattern.lower() in country.lower(), lst))
print(categorize_countries(country_list, 'stan'))
print(categorize_countries(country_list, 'ia'))
print(categorize_countries(country_list, 'island'))
print(categorize_countries(country_list, 'land'))    


#ex2.13 - analyze if there is a more elegant solution
def first_two_letters_countries(lst, n_letters):
    #create the keys, user specifies how many starting letters
    country_keys = set()
    [country_keys.add(country[0:n_letters]) for country in lst]

    #convert to dict, initialize all values to 0
    country_count = dict.fromkeys(country_keys, 0)
    for country in lst:
        for key in country_count:
            if country.startswith(key):
                country_count[key] += 1
    #why can I not do 1 liner below? I dont understand why it complains of missing []
    # [country_count[key] += 1 if country.startswith(key) for key in country_count for country in lst]
    return country_count
print(first_two_letters_countries(country_list, 4))

#ex2.14
# def first_ten_countries(*args):
#     countries = *args[0][0:11] #why unpack not allowed here?
#     # print(*args[0][0]) #why does the second space it out like this: A f g h a n i s t a n?
# print(first_ten_countries(country_list))

#is there some elegant way to use filter, this confused me a lot
def is_tenth(string):
    count = 0
    while string is not None and count <= 10:
        count += 1
        return True
    return False
first_tenth = list(filter(is_tenth, country_list))
# print(first_tenth)

#ex2.14 #ex2.15
def get_first_ten_countries(lst):
    return lst[0:10]
def get_last_ten_countries(lst):
    return lst[-10:]
print(get_first_ten_countries(country_list))
print(get_last_ten_countries(country_list))

#ex3.1
from countries_data import COUNTRY_DATA
country_dict = COUNTRY_DATA.copy()

print(f"Exercise 3 =====")
def sort_by_name(lst):
    sorted_countries = []
    for country in lst:
        sorted_countries.append(country['name'])
    return sorted(sorted_countries, key=lambda item: item[0])[:10]
print(sort_by_name(country_dict))

def sort_by_capital(lst):
    sorted_capitals = []
    for country in lst:
        sorted_capitals.append((country['name'], country['capital']))
    return sorted(sorted_capitals, key=lambda item: item[1])[:10]
#again is there some way to do this with filter
# sorted_capitals = list(filter(lambda country: country['capital'], country_dict))
print(sort_by_capital(country_dict))

DEPTH = len(country_dict) - 1
def sort_by_populsation(lst, depth=DEPTH):
    sorted_population = []
    for country in lst:
        sorted_population.append((country['name'], country['population']))
    return sorted(sorted_population, key=lambda item: item[1], reverse=True)[:depth]
print(sort_by_populsation(country_dict))

#ex3.2
def most_spoken_languages(lst):
    all_languages = []
    for country in lst:
        for language in country['languages']:
            all_languages.append(language)
    top_spoken = dict.fromkeys(set(all_languages), 0)
    for country in lst:
        for language in country['languages']:
            top_spoken[language] += 1
    top_spoken = sorted(top_spoken.items(), key=lambda item: item[1], reverse=True)[:10]
    return top_spoken
print(most_spoken_languages(country_dict))

#ex3.3
print(sort_by_populsation(country_dict, depth=10))




    
    
    








