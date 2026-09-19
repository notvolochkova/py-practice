# #ex1.1 
# for i in range(11):
#     print(i)
# count = 0
# while count <= 10:
#     print(count)
#     count += 1

#ex1.2
# for i in range(10, -1, -1):
#     print(i)
# count = 10
# while count >= 0:
#     print(count)
#     count -= 1

#ex1.3
# for i in range(1,8):
#     print(i * "#")

#ex1.4
for i in range(1, 9):
    for j in range(1, 9):
        continue
    print(8 * " #")

#ex1.5
for i in range(0, 11):
    print(f"{i} x {i} = {i*i}")

#ex1.6
skills = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for skill in skills:
    print(skill)

#ex1.7
for i in range(0, 101, 2):
    print(i)
#ex1.8
for i in range(1, 101, 2):
    print(i)

#ex2.1
all_sum = 0
for i in range(0, 101):
    all_sum += i
print(f"The sum of all numbers is {all_sum}")

#ex2.2
odd_sum = 1
even_sum = 0
for i in range(0, 101,2):
    odd_sum += (i-1)
    even_sum += i
    print(odd_sum) #gives the expected result but is it correct? Is there better way to do this?
print(f"The sum of all evens is {even_sum}, sum of all odds is {odd_sum}")

#ex3.1
#from ..05_Day_Lists import countries #you cannot do this cuz starts with a number use Pathlib
from pathlib import Path
import sys
parent = Path(__file__).resolve().parent.parent / "data" #absolute path + "data"
sys.path.append(str(parent)) #add it to Python's search list

from countries import countries
country_list = countries.copy()

land_countries = []
#works but not a very pythonic way to write I think, enumerate is one alternative
length = len(country_list)
for i in range(length):
    if 'land' in country_list[i]:
        land_countries.append(country_list[i])
print(land_countries)

#works and classic way of writing use for-each iterators
for country in country_list:
    if 'land' in country:
        land_countries.append(country)
print(land_countries)

#ex3.2 - works - is there a better way to write this?
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []
length = len(fruits) - 1
for i in range(length, -1, -1):
    reversed_fruits.append(fruits[i])
print(reversed_fruits)

#ex3.3i
from countries_data import COUNTRY_DATA
country_data = COUNTRY_DATA.copy()

#counts all languages and excludes duplicates
#Is there any better way to code this without a nested loop? I presume not as we have list of dict and inside each dict there is a list
all_languages = []
for country in country_data:
    for language in country['languages']:
        all_languages.append(language)
unique_languages = set(all_languages)
# print(unique_languages)
print(f"Total number of languages counted {len(unique_languages)}")

#ex3.3ii
top_spoken = dict.fromkeys(unique_languages, 0)
for country in country_data:
    for language in country['languages']:
        top_spoken[language] += 1 #A language from the dataset will appear no more than once in each country, i.e: you wont see "English" twice in the same list
#is there a more simpler way to write this?
top_spoken_lst = sorted(top_spoken.items(), key=lambda item: item[1], reverse=True) #sort from descending as "top most"
# print(top_spoken_lst)
print(f"Top 10 most spoken languages = {top_spoken_lst[:10]}")

#ex3.3iii
population_tuple = ()
country_list = []
for country in country_data:
    population_tuple = (country['population'], country['name'])
    country_list.append(population_tuple)
country_list.sort(reverse=True)
# print(country_list)
print(f"Top 10 most populated countries = {country_list[:10]}")