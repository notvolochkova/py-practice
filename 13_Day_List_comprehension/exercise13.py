#ex1.1
def filter_neg_zero():
    numbers = [-4,-3,-2,-1,0,2,4,6]
    numbers = [n for n in numbers if n >= 0]
    return numbers
print(filter_neg_zero())

#ex1.2
def flatten_lists():
    list_of_lists = [[1,2,3], [4,5,6], [7,8,9]]
    # print(list_of_lists[1][2])
    list_of_lists = [i for row in list_of_lists for i in row]
    return list_of_lists
print(flatten_lists())

#ex1.3
def list_of_tuples():
    col = 6
    row = 11
    def power(i):
        return lambda n : i ** n
    #solution 1 - list comprehension + generator expression + tuple unpacking
    list_of_tuples = [(i, *(power(i)(j) for j in range(col))) for i in range(row)]

    #solution 3 - list comprehension + lambda + tuple unpacking + generator expression
    # list_of_tuples = [(i, *((lambda n: i ** n)(j) for j in range(col))) for i in range(row)]

    #solution 2 - list comprehension + lambda + tuple concatenation
    # list_of_tuples = [(i,) + tuple(power(i)(j) for j in range(col)) for i in range(row)]
    return list_of_tuples
# print(list_of_tuples()) 

#ex1.4
def flatten_countries(countries):
    # flattend = [country for country_list in countries for country_pair in country_list for country in country_pair]
    # flattened = [
    #     #solution 2 - anti-pattern, works but poor implementation
    #     [country.upper(), country.upper()[:3], country_pair[1].upper()] 
    #     for country_list in countries 
    #     for country_pair in country_list
    #     for country in country_pair[:1]
    #              ]
    # return flattened
    flattened = [
        [country.upper(), country.upper()[:3], city.upper()]
        for country_list in countries
        for country, city in country_list #as we are accessing a tuple where we know there are 2 values, you can pull 2 
                ]
    return flattened
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
print(flatten_countries(countries))

#ex1.5
def list_dict_countries(countries):

    flattened = [
    {'country':country.upper(), 'city':city.upper()}
    for country_list in countries
    for country, city in country_list
            ]
    return flattened

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
print(list_dict_countries(countries))

#ex1.6
def list_1d(names):
    flattened = [
        firstname + " " + lastname
        for name_list in names
        for firstname, lastname in name_list
                ]
    return flattened
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
print(list_1d(names))

#ex1.7
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
y_intercept = lambda x1, y1, x2, y2: y1 - ((y2 - y1) / (x2 - x1)) * x1

x1, x2, y1, y2 = 2, 5, 4, 9
print(f"Slope = {slope(x1,x2,y1,y2)}")