# #ex1.1 
# # age = int(input("Enter your age="))
# # print('You are old enough to drive') if age >=18 else print(f'you need more {18 - age } years')

# #ex1.2
# my_age = 25
# your_age = int(input("Enter your age:"))
# if my_age > your_age:
#     if (my_age - your_age) == 1:
#         print('I am older than you, 1 year')
#     else:
#         print(f'I am older than you, {my_age - your_age} years')
# elif my_age < your_age:
#     if (my_age - your_age) == 1:
#         print('you are older than me, 1 year')
#     else:
#         print(f'you are older than me, {your_age - my_age} years')
# else:
#     print("we are equal, you are same age as me")

# #ex1.3
# a = int(input('Enter number one: '))
# b = int(input("Enter number two: "))
# if a > b:
#     print(f"{a} is greather than {b}")
# elif a < b:
#     print(f"{a} is smaller than {b}")
# else:
#     print(f"{a} is equal to {b}")

# #ex2.1
# score = int(input("Enter your score to get the grade = "))
# if 90 <= score <= 100:
#     print("You got an A")
# elif 80 <= score <= 89:
#     print("You got a B")
# elif 70 <= score <= 79:
#     print("You got a C")
# elif 60 <= score <= 69:
#     print("You got a D")
# elif 0 <= score <= 59:
#     print("You got an F")
# else:
#     print("invalid score")

# #ex2.2
# month = str(input("Tell me the month, and I tell you the season: "))
# if month in ['September', 'October', 'November']:
#     print("Autumn")
# elif month in ['December', "January", 'February']:
#     print("Winter")
# elif month in ['March', 'April', 'May']:
#     print("Spring")
# elif month in ['June', 'July', 'August']:
#     print("Summer")
# else:
#     print("invalid month") #basic form of check, obviously exception blocks are much better

# #ex2.3
# fruits = ['banana', 'orange', 'mango', 'lemon']
# your_fruit = str(input("Tell me the fruit: "))
# if your_fruit in fruits:
#     print(f"This fruit \'{your_fruit}\' already exists in the list")
# else:
#     fruits.append(your_fruit)
#     print(fruits)

# #ex3.1
person = {
        'first_name': 'Asabeneh',
        'last_name': 'Yetayeh',
        'age': 250,
        'country': 'Finland',
        'is_married': True,
        'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
        'address': {
            'street': 'Space street',
            'zipcode': '02210'
        }
}

# del person['skills']
import math
if 'skills' in person.keys():
    index = math.ceil((len(person['skills']) - 1) / 2)
    print(person['skills'][index])

    if 'Python' in person['skills']:
        print(person['skills'])

    if 'JavaScript' and 'React' in person['skills']:
        print("He is a front end dev")
    elif 'Node' and 'Python' and 'MongoDB' in person['skills']:
        print("He is a backend dev")
    elif 'React' and 'Node' and 'MongoDB' in person['skills']:
        print("He is a full stack dev")
    else:
        print("unknown title")

if person['is_married'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married")
