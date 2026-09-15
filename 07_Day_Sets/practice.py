
#creation
st = set()
st = {'item1', 'item2', 'item3', 'item4'}
fruits = {'banana', 'orange', 'mango', 'lemon'}

#length
print(len(st))
print(len(fruits))

#checking items
print('does this set contain item3?', 'item3' in st)
print('mango' in fruits)

#adding items
st.add('item5')
fruits.add('lime')
print(fruits)
print(st)

#add many items
st.update(['item6', 'item7'])
vegetables = ('tomato', 'onion', 'carrot', 'mushroom')
print(type(vegetables))
fruits.update(vegetables)
print(fruits)
print(type(fruits))

#removing items
st.remove('item2')
print(st)
removed = fruits.pop()
print(removed)
print(fruits)

#clearing
st.clear()
print(st)

#deletion
del st
del fruits

#convert list2set
fruits = ['banana', 'orange', 'mango', 'lemon', 'orange', 'banana']
print(fruits)
fruits = set(fruits)
print(fruits)

#joining sets - union
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage', 'onion'}
# print(fruits.union(vegetables))
# print(fruits | vegetables)
fruits.update(vegetables)
print(fruits)

#intersection
whole_numbers = {0,1,2,3,4,5,6,7,8,9,10}
even_numbers = {0,2,4,6,8,10}
print(whole_numbers.intersection(even_numbers))

#subset - superset
print(even_numbers.issubset(whole_numbers)) #all elems contained in parent set
print(whole_numbers.issuperset(even_numbers)) #all elems plus additional 

#difference in sets
print(whole_numbers.difference(even_numbers))
python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
print(dragon.difference(python))
print(python.difference(dragon))

#symmetric difference
some_numbers = {1,2,3,4,5}
print(whole_numbers.symmetric_difference(some_numbers))
print(some_numbers.symmetric_difference(whole_numbers))
print(python.symmetric_difference(dragon))
print(dragon.symmetric_difference(python))

#check if 2 sets are joint or disjoint
even_numbers = {0, 2, 4, 6, 8}
odd_numbers = {1, 3, 5, 7, 9}
even_numbers.isdisjoint(odd_numbers)


