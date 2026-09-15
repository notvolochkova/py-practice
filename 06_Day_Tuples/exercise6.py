#ex1 
empty_tuple = ()

#ex2
brothers = ('Alex', 'John', 'Alfred')
sisters = ('Mary', 'Hannah', 'Alina')

#ex3
siblings = brothers + sisters
print(siblings)

#ex4
num_siblings = len(siblings)
print(f"I have {num_siblings} siblings")

#ex5
siblings = list(siblings)
parents = ['Bob', 'Lauren']
siblings.extend(parents) #how would I handle this if I have to add it in beginning ?
family_members = tuple(siblings)
print(family_members)
print(siblings)

#ex2.1 
siblings = family_members[0:6]
print(siblings)
parents = family_members[6:]
print(parents)

#ex2.2
fruits = ('kiwi', 'orange', 'lemon', 'blueberry')
veg = ('broccoli', 'pepper', 'mushroom', 'onion')
animal_products = ('cheese', 'milk', 'yogurt', 'butter')
food_stuff_tp = fruits + veg + animal_products

#ex2.3 
food_stuff_lt = list(food_stuff_tp)

#ex2.4 - here I asume list length does not change in previous examples I made a method to handle it
print(food_stuff_lt)
# food_stuff_lt = food_stuff_lt[5:7]  
del food_stuff_lt[5:7]
print(food_stuff_lt)

food_stuff_tp = list(food_stuff_tp)
del food_stuff_tp[5:7]
food_stuff_tp = tuple(food_stuff_tp)
print(food_stuff_tp)

#ex2.5
del food_stuff_lt[0:3]
print(food_stuff_lt)
del food_stuff_lt[-4:-1] #smaller values first
print(food_stuff_lt)

#ex2.6
del food_stuff_tp

#ex2.7
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
isEstoniaNordic = 'Estonia' in nordic_countries
print(isEstoniaNordic)
isIceLandNordic = 'Iceland' in nordic_countries
print(isIceLandNordic)

#ex2.8
