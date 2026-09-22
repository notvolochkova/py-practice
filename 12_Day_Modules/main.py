
#local modules
# import mymodule 
# print(mymodule.generate_full_name('Asabeneh', 'Yetayeh'))

# from mymodule import generate_full_name, sum_two_nums, gravity, person
# print(generate_full_name('Asabeneh', 'Yetayeh'))
# print(sum_two_nums(1,9))
# mass = 100
# weight = mass * gravity
# print(weight)
# print(person['firstname'])

#local modules renamed
from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g
print(fullname('Asabeneh', 'Yetayeh'))
print(total(1,9))
mass = 100
weight = mass * g
print(weight)
print(p)
print(p['firstname'])
print(p['country'])

#os module
import os
# os.rmdir('path_dir')
# os.mkdir('path_dir') if FileNotFoundError else os.chdir('path_dir')
print(os.getcwd()) #D:\Code\Python_Learning

#sys module
import sys
# print('Welcome {}. Enjoy {} challenge!'.format(sys.argv[1], sys.argv[2]))
# print(sys.argv[0], sys.argv[1], sys.argv[2])
print(sys.argv)
print(type(sys.argv))
# print(len(sys.argv))

# sys.exit()
print(sys.maxsize) #9223372036854775807

#adding a sibling-level directory to the sys.path
from pathlib import Path
parent = Path(__file__).resolve().parent.parent / "data"
sys.path.append(str(parent)) 

#Python environment path
print(sys.path) #environment path

#version, prints the uv environment information
print(sys.version) #3.14.7 (main, ) [MSC v.1944 64 bit (AMD64)]

#statistics module
from statistics import *
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))
print(median(ages))
print(mode(ages))
print(stdev(ages))

#math module
print(f"Math modules")
# import math 
# print(math.pi)
# print(math.sqrt(2))
# print(math.pow(2, 3)) #format is x^y = math.pow(x,y)
# print(math.floor(9.81))
# print(math.ceil(9.81))
# print(math.log10(100))
# from math import pi
# print(pi)

# from math import pi, sqrt, pow, floor, ceil, log10
# print(pi)
# print(sqrt(2))
# print(pow(2,3))
# print(floor(9.81))
# print(ceil(9.81))
# print(log10(100))

from math import pi as PI
print(PI)

#string module
import string
print(string.ascii_letters)
print(string.digits)
print(string.punctuation)

#random module
from random import random, randint
print(random()) #returns value between 0 and 0.99 -> 1
print(randint(5, 20))

