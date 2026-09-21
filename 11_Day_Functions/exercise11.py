#ex1.1
def add_two_numbers(num1, num2):
    return num1 + num2
print(add_two_numbers(num1=99, num2=35))

#ex1.2
def area_of_cirlce(r):
    PI = 3.14
    return PI * (r**r)
print(area_of_cirlce(5))

#ex1.3
def add_all_nums(*args):
    total = 0
    for i in range(len(args)):
        # if type(args[i]) != type(3):
        if type(args[i]) is not int:
            print(f"Element \'{i}\' with value: \'{args[i]}\', terminating!")
            break
            #exit(1) #terminates the program
        else:
            total += args[i]  
    print(f"Sum of all numbers computed so far: {total}")
    return total
add_all_nums(1,98,'e',45)

#more python and better way to write this
def add_all_nums2(*args):
    total = 0
    for arg in args:
        if not isinstance(arg, int):
            print(f"Element \'{arg}\' is not an integer, terminating!")
            break
        else:
            total += arg
    print(f"Sum of all numbers computed so far: {total}")
    return total
add_all_nums2(1,2,8,'e',34)

#ex1.4
def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = 0
    if not isinstance(celsius, int):
        print(f"{celsius} is not a in integer, re-try again")
        exit(1) #breaks can only be used within loops
    else:
        fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
print(convert_celsius_to_fahrenheit(45))

#ex1.5 - basically a repeat of exercise9
def check_season(month):
    month = month.lower().strip()
    if month in ['september', 'october', 'november']:
        return "Autumn"
    elif month in ['december', "january", 'february']:
        return "Winter"
    elif month in ['march', 'april', 'may']:
        return "Spring"
    elif month in ['june', 'july', 'august']:
        return "Summer"
    return "Invalid month"
print(check_season('vanilla'))

#more pythonic and better way to write this is via a dictionary
def check_season(month):
    seasons = {
        "september": "Autumn",
        "october": "Autumn",
        "november": "Autumn",
        "december": "Winter",
        "january": "Winter",
        "february": "Winter",
        "march":"Spring",
        "april":"Spring",
        "may":"Spring",
        "june":"Summer",
        "july":"Summer",
        "august":"Summer",
    }
    return seasons.get(month.lower().strip(), "Invalid Month")
print(check_season("September"))
print(check_season("vanilla"))

#ex1.6
def calculate_slope(equation):
    #expect y = mx + b
    equation = list(equation.split())
    print(equation)
    # index = equation.index('x')
    # slope = equation[index]
    slope = equation[2]
    slope = slope.split('x')[0]
    print(f"Slope of the provided linear equation = \'{slope}\'")
    return int(slope)
print(calculate_slope('y = 9x - 11'))

#ex1.7
def solve_quadratic_eqn(equation):
    #assume we always obtain ax^2 + bx + c = 0
    pass

#ex1.8
def print_list(input_list):
    for elem in input_list:
        print(elem)
    return None
print_list([1,2,3,4,'hello'])

#ex1.9
def reverse_list(input_list):
    reversed = []
    for i in range(len(input_list) - 1, -1, -1):
        reversed.append(input_list[i])
    return reversed
    #best way of doing this is as below, 1 line and clean
    # return input_list[::-1]   
new_lst = reverse_list(['jupiter', 'mars', 'pluto', 'mercury'])
print(new_lst)

#ex1.10
def capitalize_list_items(input_list):
    ret_list = []
    for elem in input_list:
        ret_list.append(elem.capitalize())
    return ret_list
print(capitalize_list_items(['jupiter', 'mars', 'pluto', 'mercury']))

#ex1.11
# def add_item(input_list, item):
#     return input_list.append(item.capitalize())
def add_item(input_list, item):
    ret_list = []
    ret_list = input_list + [item]
    return ret_list

food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
numbers = [2,3,7,9]
# print(add_item(food_stuff, 'Meat'))     
# print(add_item(numbers, 5))

#ex1.12
def remove_item(input_list, item):
    index = input_list.index(item)
    del input_list[index]
    return input_list
print(remove_item(food_stuff, 'Mango'))
print(remove_item(numbers, 3))

#ex1.13
def sum_of_numbers(arg):
    total = 0
    for i in range((arg+1)):
        total += i
    return total
print(sum_of_numbers(5))
print(sum_of_numbers(10))
print(sum_of_numbers(100))

#ex1.14
def sum_of_odds(arg):
    total_odds = 0
    for i in range(1,(arg+1), 2):
        total_odds += i
    return total_odds
print(sum_of_odds(9))

#ex1.15
def sum_of_evens(arg):
    total_evens = 0
    for i in range(0, (arg+1), 2):
        total_evens += i
    return total_evens
print(sum_of_evens(10))


#ex2.1
def evens_and_odds(arg):
    num_odds = 0
    num_evens = 0
    for i in range(0, (arg+1), 1):
        if i % 2 == 0:
            num_evens += 1
        else:
            num_odds += 1
    print(f"The number of odds are {num_odds}\nThe number of evens are {num_evens}")
    return (num_odds, num_evens)
print(evens_and_odds(100))

#ex2.2
def factorial(arg):
    arg = int(arg) #in case there is float
    product = 1
    for n in range(1,(arg+1),1): 
        product *= n
    return product
print(factorial(11))

#ex2.2
def is_empty(arg):
    return True if len(arg) == 0 else False
    # if len(arg) == 0:
    #     return True
    # else:
    #     return False
print(is_empty([]))
print(is_empty({}))
print(is_empty(()))
print(is_empty(''))
print(is_empty((500,)))

#ex2.4
def greet(name='Guest'):
    print(f"Hello, {name}!")
greet()
greet("Alice")

#ex2.5
def show_args(**arg):
    print(f"Received:", end=" ")
    for k, v in arg.items():
        print(f"{k}: {v},", end=' \n')
show_args(name="Alice", age=30, city="New York")
show_args(name="Bob", pet="Fluffy, the bunny")

#ex3.1 - not correct and not workings
# import math
# def is_prime(arg):
#     arg = int(arg)
#     for i in range(1,(arg+1),1):
#         if arg % i == 0:
#             return False
#         else:
#             return True
# print(is_prime(2))

#ex3.2
def is_all_unique(input_list):
    if not isinstance(input_list, list):
        print(f"Supplied input is not a list type!, terminating")
        exit(1)
    for elem in input_list:
        count = input_list.count(elem)
        if count > 1:
            return False
        elif count <= 1:
            continue
    return True
# print(is_all_unique('hello'))
print(is_all_unique([1,2,3,4,5,'hello']))
print(is_all_unique([1,2,3,5,5,'hello']))

#ex3.3
def is_all_same_type(input_list):
    if not isinstance(input_list, list):
        print(f"Supplied input is not a list type!, terminating")
        exit(1)
    elem_type = type(input_list[0])
    if all(isinstance(elem, elem_type) for elem in input_list):
        return True
    else:
        return False
print(is_all_same_type([1,2,3,3,'e']))

#ex3.4
import keyword
def valid_name(arg):
    arg = str(arg).lower()
    if arg.isidentifier() and not keyword.iskeyword(arg):
        return True
    else:
        return False
print(f"exercise 3.4")
print(valid_name('my_var'))
print(valid_name('for'))
print(valid_name('str()'))
print(valid_name('price$'))
print(valid_name('user-name'))
print(valid_name('134player'))
print(valid_name('user name'))
print(valid_name('user@name'))

#ex3.5
from pathlib import Path
import sys
parent = Path(__file__).resolve().parent.parent / "data" #absolute path + "data"
sys.path.append(str(parent)) #add it to Python's search list

from countries_data import COUNTRY_DATA
country_data = COUNTRY_DATA.copy()

def most_spoken_languages(depth=10):
    all_languages = []
    for country in country_data:
        for language in country['languages']:
            all_languages.append(language)
    unique_languages = set(all_languages)
    top_spoken = dict.fromkeys(unique_languages, 0)
    for country in country_data:
        for language in country['languages']:
            top_spoken[language] += 1 
    top_spoken = dict(sorted(top_spoken.items(), key=lambda item: item[1], reverse=True)) 
    most_spoken_list = []
    for k, v in top_spoken.items():
        most_spoken_list.append(k)
    return most_spoken_list[:depth]
print(most_spoken_languages())
print(most_spoken_languages(depth=20))

#ex3.6
def most_populated(depth=10):
    population_tuple = ()
    country_list = []
    for country in country_data:
        population_tuple = (country['population'], country['name'])
        country_list.append(population_tuple)
    country_list.sort(reverse=True)
    most_populated_list = [item[1] for item in country_list[:depth]]
    return most_populated_list
print(most_populated())
# print(most_populated(depth=20))

