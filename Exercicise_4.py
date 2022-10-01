# Pattern printing
#  take an integer and boolean input
# for boolean true pattrn is
#  x
#  x x
#  x x x
#  x x x x
# for boolean false pattern is
# x x x x
# x x x
# x x
# x

num = int(input("enter a number for * pattern"))
choice = int(input(" enter 1 or 0"))
i = 0
if choice == 0:
    while (i <= num):
        print(" * " * (num - i) + " " * i)
        i += 1
elif choice == 1:
    while (i <= num):
        print(" * " * i + " " * (num - i))
        i += 1
else:
    print("your input can't be processed")
