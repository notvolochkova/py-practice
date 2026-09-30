#below code will invoke the Python type errors based on category
def name_error():
    try:
        print(first_name)
    except NameError as e:
        print(f"[NameError] -> {e}")

def syntax_error():
    try:
       eval("print hello world") 
    except SyntaxError as e:
        print(f"[SyntaxError] -> {e}")

def index_error():
    try:
        numbers = [1,2,3]
        print(numbers[10])
    except IndexError as e:
        print(f"[IndexError] -> {e}")

def module_error():
    try:
        import maths
    except ModuleNotFoundError as e:
        print(f"[ModuleNotFoundError] -> {e}")

def attribute_error():
    try:
        import math
        print(math.PI)
    except AttributeError as e:
        print(f"[AttributeError] -> {e}")

def key_error():
    try:
        users = {'name':'Asab', 'age':250, 'country':'Finland'}
        print(users['children'])
    except KeyError as e:
        print(f"[KeyError] -> {e}")

def type_error():
    try:
        value = 4 + '3'
        print(value)
    except TypeError as e:
        print(f"[TypeError] -> {e}")

def import_error():
    try:
        from math import power
    except ImportError as e:
        print(f"[ImportError] -> {e}")

def value_error():
    try:
        value = '12a'
        return int(value)
    except ValueError as e:
        print(f"[ValueError] -> {e}")

def zero_error():
    try:
        print(13/0)
    except ZeroDivisionError as e:
        print(f"[ZeroDivisionError] -> {e}")

def main():
    name_error()
    syntax_error()
    index_error()
    module_error()
    attribute_error()
    key_error()
    type_error()
    import_error()
    value_error()
    zero_error()
    
if __name__ == "__main__":
    main()
