
#ex1.1
from random import randint
from string import ascii_letters, digits
#I assume the user_id here is alphanumeric but does not contain punctuations
def random_user_id(user_id_length=6):
    CHARACTER_POSSIBILITIES = ascii_letters + digits
    user_id = ''
    for i in range(user_id_length):
        index = randint(0, len(CHARACTER_POSSIBILITIES) - 1 )
        user_id += CHARACTER_POSSIBILITIES[index]
    return user_id
print(random_user_id())

#ex1.2
def user_id_gen_by_user():
    user_id_length = int(input("Input the length of each user_id to be generated: "))
    num_user_id = int(input("Input the required number of user_id to be generated: "))

    user_id_list = []
    for i in range(num_user_id):
        user_id = random_user_id(user_id_length) 
        user_id_list.append(user_id)
    return user_id_list
print(user_id_gen_by_user())

#ex1.3
def rgb_color_gen():
    rgb_tuple = tuple(randint(0, 255) for i in range(3))
    color_str = "rgb" + str(rgb_tuple) + ""
    return color_str
print(rgb_color_gen())

#ex2.1
def list_of_hexa_colors(num_of_colors=1):
    hex_length = 6
    HEX_CHARACTERS = digits + ascii_letters[:6] 
    hex_color = ""
    hex_list = []

    for i in range(num_of_colors):
        for j in range(hex_length):
            index = randint(0, len(HEX_CHARACTERS) - 1)
            hex_color += HEX_CHARACTERS[index]
        hex_list.append("#"+hex_color)
        hex_color = ""
    return hex_list
    
print(list_of_hexa_colors())
print(list_of_hexa_colors(5))

#ex2.2
def list_of_rgb_colors(num_of_colors=1):
    rgb_list = []

    for i in range(num_of_colors):
        rgb_color = rgb_color_gen()
        rgb_list.append(rgb_color)
        rgb_color = "" #reset it to not keep appending 
    return rgb_list
print(list_of_rgb_colors())
print(list_of_rgb_colors(3))

#ex2.3
def generate_colors(color_choice='rgb', num=1):
    if color_choice == 'rgb':
        return list_of_rgb_colors(num)
    elif color_choice == 'hexa':
        return list_of_hexa_colors(num)
    else:
        return "Invalid entry"
print(f"last exercise")
print(generate_colors())
print(generate_colors('hexa', 3))
print(generate_colors('hexa', 1))
print(generate_colors('rgb', 3))
print(generate_colors('rgb', 1))

#ex3.1 - wrong
# def shuffle_list(lst):
#     lst_length = len(lst) - 1
#     shuffled = ['3']
#     for i in range(lst_length+1):
#         index = randint(0, lst_length)
#         print(index)
#         if lst[index] not in shuffled:
#             shuffled[i] = lst[index]
#         else:
#             index = randint(0, lst_length)
#     print(shuffled)
# print(shuffle_list(['cat', 'dog', 'rat', 'mouse']))

#https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle
def shuffle_list(input_list):
    shuffled = input_list.copy()
    n = len(shuffled)
    for i in range(n - 1, 1, -1):
        j = randint(0, i)
        #a, b = b, a
        shuffled[j], shuffled[i] = shuffled[i], shuffled[j]
    return shuffled
print(shuffle_list(['cat', 'dog', 'rat', 'mouse', 'ed']))

#wrong implementation
# def random_num(length=7):
#     num = randint(0,9)
#     lst = []
#     lst.append(num)
#     for n in range(length - 1):
#         if (lst.count(num) > 1) in lst:
#             index = lst.index(num)
#             lst.remove(index)
#         num = randint(0,9)
#         lst.append(num)
#     return lst
# print(random_num())
#ex3.2
def random_num(length=7):
    if length > 10:
        return "You cannot have unique numbers of 0-9 if the length is > 10"
    lst = []
    #only add the number if it is not already in the list
    while len(lst) < length:
        num = randint(0, 9)
        if num not in lst:
            lst.append(num)
    return lst
print(random_num())
print(random_num(11))

