# def print2(str1):
#     print("This is ", str1)


# print2("amit")

"""
:param n
return n*(n-1)*(n-2)*......*3*2*1
n! = n*(n-1)*(n-2)*......*3*2*1
n! = n*(n-1)!
"""


#
# def factorial_iterative(n):
#     fac = 1
#     for i in range(0, n):
#         fac *= (i + 1)
#
#
# number = int(input("Enter the number"))
# print(factorial_iterative(number))
#
#
# def factorial_recursive(n):
#     if n == 1 or n == 0:
#         return 1
#     else:
#         return n * factorial_recursive(n - 1)
#
#
# number1 = int(input("Enter the number1"))
# print(factorial_recursive(number1))


def fibonacci_sequence(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_sequence(n - 1) + fibonacci_sequence(n - 2)


fib_number = int(input("enter no. for fibonacci sequence"))
print(fibonacci_sequence(fib_number))
