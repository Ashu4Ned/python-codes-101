string1 = "Amar is a good boy"
print(string1)
print(string1[0:5])
# This is called string slicing
print(len(string1))
# This method is to check length of string
print(string1[0:78])
# THis won't give error this will print up to availability = print(string1[0:])
print(string1[0:5:2])
print(string1[::])
# =print(string1[0:18:1])

# Using negative slicing
print(string1[-4:-9])

"""
-12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
M    O    N  T  Y     P  Y  T  H  O  N
0    1    2  3  4  5  6  7  8  9  10 11

Written above is the slicing method

"""
# Some important functions on string
print(string1.isalnum())
""".isalnum() this checks whether contains a number or not 
and returns boolean values true or false
"""
print(string1.isalpha())
""" .isalpha() this checks whether contains alphanumeric or not and 
returns boolean values true or false
"""
print(string1.endswith("boy"))
""".endswith() this checks whether ends with given string or not and 
returns boolean values true or false
"""
print(string1.count("a"))
""".count() this checks number of given letter in string and returns int"""
print(string1.capitalize())
# .capitalize() this makes the first character uppercase
print(string1.find("is"))
# .find() this finds character given to search
print(string1.upper())
# .upper() converts the total string to upper case
print(string1.lower())
# .lower() converts the total string to lower case
print(string1.replace("Amar", "Rajan"))
# .replace() replaces one character with other
