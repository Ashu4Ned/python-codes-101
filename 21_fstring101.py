# F STRINGS
import math

me = "asdg"
a1 = 3
# a = "this is %" % (me, a1)
# b = a.format(me, a1)

a = f"this is {me} {a1}"
print(a)
b = f"the value of cos 120 is {math.cos(120)}"
print(b)
