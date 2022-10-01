# there are 4 types of operators
# 1. Arithmetic operator
# 2. Assignment operator
# 3. Comparison operator
# 4. Logical operator
# 5.Identity operator
# 6. Bitwise operator


#       ARITHMETIC OPERATOR
print("5 + 6 is", 5 + 6)
# (+) is the addition operator
print("5 - 6 is", 5 - 6)
# (-) is the subtraction operator
print("5 * 6 is", 5 * 6)
# (*) is the multiplication operator
print("15 / 6 is", 15 / 6)
# (/) is the division operator
print("15 // 6 is", 15 // 6)
# (//) is the floor division operator
print("5 ^ 6 is", 5 ** 6)
# (**) is the exponential operator
print("5 % 6 is", 5 % 6)
# (%) is modulo operator


#       ASSIGNMENT OPERATOR
print("assignment operators")
x = 12
x += 2
print(x)
x -= 3
print(x)
x *= 3
print(x)
x /= 3
print(x)
x %= 3
print(x)

#      COMPARISON OPERATOR
print("Comparison operator")
i = 5
print(i == 5)
print(i != 5)
print(i > 5)
print(i >= 5)
print(i < 5)
print(i <= 5)

#       LOGICAL OPERATOR
print("Logical operator")
a = True
b = False

print(a and b)
print(a and a)
print(b and b)
print(a or b)
print(a or a)
print(b or b)
print(a is b)
print(a is not b)
print(3 is 5)
print(3 is not 2)

#       MEMBERSHIP OPERATOR
print("Membership operator")
list = [3, 3, 2, 2, 39, 33, 35, 32]
print(32 in list)
print(324 not in list)
print(32 not in list)

#       BITWISE OPERATOR
print("Bitwise operator")
# 0 - 00
# 1 - 01
# 2 - 10
# 3 - 11
print(0 & 1)
print(0 & 0)
print(1 & 1)
print(0 | 1)
print(0 | 0)
print(1 | 1)