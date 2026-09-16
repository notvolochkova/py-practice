
empty_dict = {}
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3'}

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': '250',
    'country': 'Finland',
    'is_married': True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street':'Space street',
        'zipcode':'3977'
    }
}

#length
print(len(person))

#accessing elements
print(person['first_name'])
print(person['country'])
print(person['skills'])
print(person['skills'][0])
print(person['address']['street'])
# print(person['city']) #KeyError: 'city'

print(person.get('first_name'))
print(person.get('country'))
print(person.get('city')) #returns None, this key does not exist

#adding items
person['job_title'] = 'Instructor'
person['skills'].append('HTML')
print(person)

#modifying items
person['first_name'] = 'Eyob'
person['age'] = 252
print(person)

#checking keys
print('skills' in person)
print('yearly_income' in person)

#removing an item
person.pop('first_name')
# print(person)
person.popitem()
# print(person)
del person['is_married']

#dct to list of tuples
items = person.items()
print(items)
print(type(items))

#clears the dictionary
# print(person.clear())

#deletion
# print(person)
# del person

#copy
new_person = person.copy()
# print(new_person)

#get dictionary keys
keys = person.keys()
print(keys)
print(type(keys))
print(person.values())
print(type(person.values()))






