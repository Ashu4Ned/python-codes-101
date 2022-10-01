# var1 = 6
# var2 = 56
# print("Enter a number")
# var3 = int(input())
#
# if var3 > var2:
#     print("Greater")
# elif var3 == var2:
#     print("equal")
# else:
#     print("Lesser")
#
# list1 = [5, 6, 9, 11, 7]
#
# if 5 in list1:
#     print("yes")
#
# if 77 not in list1:
#     print("No, it is not")
#
# print("enter the number to check whether present in list or not")
# c1 = int(input())
# if c1 in list1:
#     print("yes it is in the list")
# else:
#     print("no it is not in the list")

# program to take input user age and print whether they are eligible to drive or not
# print("Please, enter your name")
# name = str(input())
# print("Please, enter your age")
# age_of_user = int(input())
# if 18 <= age_of_user <= 75:
#     print("Hello, " + name + " You are eligible to drive a vehicle")
# elif not age_of_user > 7 >= 18:
#     print("Sorry, " + name + " you are not eligible to drive")
# else:
#     print(".....")
#
# # SHORT HAND NOTATION
a = int(input("Enter a\n"))
b = int(input("Enter b\n"))

# if a > b: print(" a is greater than b")
print("a is greater than b ") if a > b else print(" a is lesser than b")
