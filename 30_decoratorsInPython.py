# def function1():
#     print("join me")
#
#
# func2 = function1()
# del function1
# func2()

#
# def func_ret(num):
#     if num == 0:
#         return print
#     if num == 1:
#         return sum
#
#
# a = func_ret(0)
# print(a)
# # In func_ret() we used built-in functions inside a function
# # also we can do new functions inside other using decorators
#
# def executor(func):
#     func("This")
#
# executor(print)

# ------------DECORATOR---------

def dec1(func1):
    def nowexec():
        print("Executing now")
        # we can do anything in pace of print
        func1()
        print("Executed")

    return nowexec


@dec1
def Who_are_you():
    print("You are a good boy")

# Who_are_you = dec1(Who_are_you)
# this is decorator

