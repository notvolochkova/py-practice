# #while loops
# count = 0
# while count < 5:
#     print(count)
#     count += 1
# else:
#     print(f"i exited the loop! bcuz 5 is not < {count}")

# print("out of it")

# #break - abruptly terminate the iteration
# count = 0
# while count < 5:
#     print(count)
#     count += 1
#     if count == 3:
#         break

#continue - you can skip some iterators
# count = 0 
# while count < 5:
#     if count == 3:
#         count += 1
#         continue
#     print(count)
#     count += 1

#for in lists
numbers = [0,1,2,3,4,5]
for number in numbers:
    print(number)

#for in strings
language = 'Python'
for letter in language:
    print(letter)

for i in range(len(language)):
    print(language[i])

#for loop on tuple
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
#for loop in dict
for key in person:
    print(person[key])
for key in person:
    print(key)
for key, value in person.items():
    print(key, value)

#for in set - will skip duplicates and order of print changes
it_companies = {'Facebook', 'Google', 'IBM','Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)

#break 
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break

#continue
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end")
print('outside the loop')

#range
lst = list(range(11))
print(lst)

st = set(range(1,11))
print(st)

lst = list(range(0,11,2))
print(lst)

st = set(range(0,11,2))
print(st)

lst = list(range(11, 0, -2)) #basically gives a list of numbers but in reverse
print(lst)

#range with for
# for number in range(11):
#     print(number)

#nested for loops
for x in range(10):
    print(x,"in x ")
    for y in range(10):
        print(y, "in y")

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)

#for else
for number in range(11):
    print(number)
else:
    print('The loop stops at', number)

#pass
for number in range(6):
    pass