# 1
# To make a faulty calculator for the expressions 45*3, 56+9, 56/6
# It will give output 555, 77, 4


choice = [1, 2, 3, 4]
x = int(input("Enter first no"))
y = int(input("Enter sec no"))
print("enter the operation in 1,2,.. 1.add, 2.subtract, 3.multiply 4.divide")
c = int(input())
if c in choice:
    if c == 3 and x == 45 and y == 3:
        print(555)
    elif c == 1 and x == 56 and y == 9:
        print(77)
    elif c == 4 and x == 56 and y == 6:
        print(4)
    elif c == 1:
        print(x + y)
    elif c == 2:
        print(x - y)
    elif c == 3:
        print(x * y)
    elif c == 4:
        print(x / y)
    else:
        print("error")
else:
    print("404 error")
