# f = open("text", "w")
# a = f.write("--My wish is always with you\n")
# print(a)
# #  this w is for write mode
# # this print line prints no of characters input
#
# f = open("text","a")
# b = f.write("This line is appended")
# print(b)
# this a is for append mode
# this print line prints no of characters input

# this is how we doo both reading and writing
c = open("text", "r+")
print(c.read())
c.write("\n thank you")

c.close()
