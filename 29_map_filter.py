# ---------------------MAP-----------------------------------

numbers = ['3', ' 2', '4', '67', '45', '63', '43', '98']

# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
# we can do the above thing using map function
# map helps in typecasting as well as applying functions to our list

numbers = list(map(int, numbers))

numbers[2] = numbers[2] + 1
print(numbers[2])

num = [2, 3, 4, 5, 6, 7, 8, 9, 10]


def sq(x):
    return x * x


squared_list_Of_Num_using_square_function = list(map(sq, num))
print("we are printing using square function", squared_list_Of_Num_using_square_function)

# we did the above task using function whereas now we will do the same using lambda

squared_list = list(map(lambda x: x * x, num))
print("Here we are printing using lambda and o/p is same", squared_list)


def square(a):
    return a ** 2


def cube(a):
    return a ** 3


func = [square, cube]
for i in range(5):
    val = list(map(lambda x: x(i), func))
    print(val)

# --------------------FILTER--------------------------------
# Filter function filters from list and returns true or false

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def is_greater_5(num):
    return num > 5


gr_than_5 = list(filter(is_greater_5, list1))
print(gr_than_5)

# -----------------REDUCE---------------------
from functools import reduce

list2 = [1, 2, 3, 4, 5]
# to add all the elements of list2 we can use loop

# n = 0
# for i in list2:
#     num += i
# print(num)

# Instead of using for loop we will use reduce function to do same task in 1 line

add = reduce(lambda a, b: a + b, list2)
print(num)
