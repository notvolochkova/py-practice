
#ex1.1
dog = {}
print(type(dog))

#ex1.2
dog['name'] = 'Sparky'
dog['color'] = 'Black'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 5
print(dog)

#ex1.3
student = {
    'first_name': 'Hannah',
    'last_name': 'Fox',
    'sex': 'F',
    'age':'29',
    'martial_status':'single',
    'skills':['Linguistics','German', 'French', 'Arabic'],
    'country':'Netherlands',
    'city':'Amsterdam',
    'address': {
        'street':'stulz',
        'house_no':43
    }
}
print(student)

#ex1.4
num_elem = len(student)
print(num_elem)

#ex1.5
skills = student['skills']
print(skills)
print(type(skills))

#ex1.6
skills += ['Math'] + ['Geography'] #is there another way to write this or better way?
print(skills)
student['skills'].append(skills)
print(student)

#ex1.7
student_k = student.keys()
print(student_k)

#ex1.8
student_v = student.values()
print(student_v)

#ex1.9
student_tpl = student.items()
print(student_tpl)

#ex1.10
del student['martial_status']
print(student)

#ex1.11
print(student_tpl)
del student_tpl

