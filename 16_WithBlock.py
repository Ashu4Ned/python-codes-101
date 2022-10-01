a = 12
# this a is global variable
"""
Opening a file using with block and we do not have to separately open or close as 
 with block does all that for us
"""
with open("text.txt") as f:
    a = f.readlines()
    # this a is local variable
    # f.readlines() reads all lines
    print(a)
# f = open("text.txt", "rt")
# old method
