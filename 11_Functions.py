a = 9
b = 8
c = sum((a, b))
print(c)

# builtin function


def function1(a, b):
    print("Welcome to function 1", a + b)


function1(5, 8)


# print(function1())

def function2(a, b):
    """This is a function to calculate average.
    This does not work for more than 2 nos."""
    average = (a + b) / 2
    # print(average)
    return average


v = function2(8, 6)
print(v)
print(function2.__doc__)
# this prints docstring of function2
"""
A python docstring is a string module,class,function or
method,so we programmers can understand what it does without 
having to read the details of implementation
"""
