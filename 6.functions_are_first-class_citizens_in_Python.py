
# Functions are first-class citizens in Python:

# They can be passed as arguments to other functions,
# returned as values from other functions, and
# assigned to variables and stored in data structures.

def coco():
    return 3


def wawa(a):
    return_value_of_a_function = a() # we passed coco function as a parameter
    return "life"


def myfunc(a, b):
    return a + b

funcs = [myfunc]
funcs[0]
funcs[0](2, 3)

if __name__ == '__main__':
    functions_list = []
    functions_list.append(coco) # we appended the coco function as a memeber of a list
    ddd = wawa(coco)
    print("")