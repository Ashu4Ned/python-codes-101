# Files io basics
"""
"r"- reading mode - open for file reading - default mode
"w" - writing mode
"x" - exclusive creation create file if it does not exist
"a" - append - add more content to file
"t" - text mode
"b" - binary mode
"+" - to both write and read
"""

f = open("text")
content = f.read()
print(content)
# this function to read the text
f.close()

g = open("text", "r+")
# cont = g.read() if file is read then read line function can't be optimally used
# for line in cont:
#      print(line)
# this for loop to print each character of text file


for line in g:
    print(line, end="")
# this for loop prints text line by line

print(g.readlines())
print(g.readline())
print(g.readline())
print(g.readline())
