f = open("text.txt")
print(f.tell())
# f.tell shows the position of pointer
print(f.readline())
print(f.tell())
print(f.readline())
# f.readline() reads line by line
print(f.tell())
f.seek(10)
# this resets the pointer to input line
f.close()
print()