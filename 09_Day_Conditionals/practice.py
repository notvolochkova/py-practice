
a = 3
#if
if a > 0:
    print('A is a positive number')

#if-else
a = 3
if a < 0:
    print("A is a negative number")
else:
    print("A is a positive number")

#elif
a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')

#short hand if else
a = 3
print('A is positive') if a > 0 else print('A is negative')

#nested if conditions
a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zeroooo')
else:
    print('A is a negative number')

#using and logical operator
z = 4
if z > 0 and z % 2 == 0:
    print('z is even and a positive integer')
elif z > 0 and z % 2 != 0:
    print('z is odd and a positive integer')
elif a == 0:
    print('z is zero')
else:
    print('z is negative')

#using if logical operator
user = 'James'
access_level = 4
if user == 'admin' or access_level >= 4:
    print('Access granted!')
else:
    print('Access denied!')