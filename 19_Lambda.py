# Lambda function or anonymous function

minus = lambda x, y: x - y
print("9 - 7 = ", minus(9, 7))


# Written above syntax is also similar to this syntax
def minus(x, y):
    return x - y


# more use of lambda

a = [[1, 6], [6, 14], [4, 8]]
a.sort(key=lambda x: x[1])
a.sort(key=lambda x: x[0])
print(a)

# the "key" keyword is used to take a function as input
