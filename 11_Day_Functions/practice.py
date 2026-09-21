
#function without params and without return values
# def generate_full_name():
#     first_name = 'Asabeneh'
#     last_name = 'Yetayeh'
#     space = ' '
#     full_name = first_name + space + last_name
#     print(full_name)
# generate_full_name()

# def add_two_numbers():
#     num_one = 2
#     num_two = 3
#     total = num_one + num_two
#     print(total)
# add_two_numbers()

#function with returns
def generate_full_name():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = " "
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())

def add_two_numbers():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total
print(add_two_numbers())

#function with params
def greetings(name):
    message = name + ", welcome to Python for Everyone!"
    return message
print(greetings('Asabeneh'))

#functions with single params
def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))

def square_number(x):
    return x * x
print(square_number(2))

def area_of_circle(r):
    PI = 3.14 #constants are suggested to be capitalized as per PEP
    area = PI * square_number(r)
    return area
print(area_of_circle(10))

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total += i
    return total
print(sum_of_numbers(10))
print(sum_of_numbers(100))

#function with multiple params
def generate_full_name(first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print('Full name: ', generate_full_name('Asabeneh', "Yetayeh"))

def sum_two_numbers(num_one, num_two):
    sum = num_one + num_two
    return sum
print('Sum of two numbers:', sum_two_numbers(1, 9))

def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age
print('Age: ', calculate_age(2021, 1819))

def weight_of_object(mass, gravity):
    weight = str(mass * gravity)+ ' N'
    return weight
print('Weight of an object in Netwons: ',weight_of_object(100, 9.81))

#passing args with k-v pairs
def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname + space + lastname
    print(full_name)
print_fullname(firstname='Asabeneh', lastname='Yetayeh')
print_fullname('perez', 'maddy') #order does matter here cause we dont specify the 'key'

def add_two_numbers(num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(num2 = 3, num1 = 2))

#function returns pt 2 - returning a str
def print_name(first_name):
    return first_name

ret_name = print_name('Asabeneh')
print(ret_name)
def print_full_name(first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
ret_full = print_full_name(first_name='Asabeneh', last_name='Yetayeh')
print(ret_full)

#returning an integer
def add_two_numbers(num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(2,3))

def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age
print('Age: ', calculate_age(2019, 1819))

#returning a boolean
def is_even(n):
    if n % 2 == 0:
        return True
    return False
print(is_even(10))
print(is_even(11))

#returning a list
def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))

#passing default values
def greetings(name = 'Peter'):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings())
print(greetings('Asabeneh'))

def generate_full_name(first_name='Asabeneh', last_name='Yetayeh'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())
print(generate_full_name(first_name='Sally', last_name='Walker'))

def calculate_age(birth_year, current_year = 2026):
    age = current_year - birth_year
    return age
print('Age: ', calculate_age(1983))

def weight_of_object(mass, gravity=9.81):
    weight = str(mass * gravity)+ ' N'
    return weight

print('Weight of an obj in Netwons: ', weight_of_object(100))
print('Weight of an obj in Netwons: ', weight_of_object(100, 1.62))

#arbitrary number of arguments
def sum_all_numbers(*nums):
    total = 0
    for num in nums:
        total += num
    return total
print(sum_all_numbers(2,3,5,1,1,1,1))

#def and aribitrary params in func
def generate_groups(team, *args):
    print(team)
    for i in args:
        print(i)
generate_groups('Team-1', 'Asabeneh', 'Brook', 'David', 'Eyob')

#dict unpacking
def greet(name, location):
    print("Hi there", name, "how is the weather in", location)
greet(name='Alice', location="New York")
my_dict = {"name": "Kelly", "location":"New York"}
greet(**my_dict)

#arbitrary number of named arguments
def arbitrary_named_args(**args):
    print("I have received an arbitrary number of arguments, totaling", len(args))
    print("They are provided as a dictionary in my function:", type(args))
    print("let's print them: ")
    for k, v in args.items():
        print(" * key:", k, "value:", v)
arbitrary_named_args()

#passing functions as parameters
def square_number(n):
    return n ** n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3))





