grocery = ["Lentil", "Rice", "Pepper", "Hot Sauce", "Ketchup", "Spices", 56, 93.4]
# this is a list format like array in java
print(grocery)
print(grocery[5])
numbers = [89, 65, 45, 75, 82, 98, 34]
print(numbers)
# .sort() is used to sort the list in order
numbers.sort()
print(numbers)
# .reverse() function is to reverse the list
numbers.reverse()
print(numbers)
# list slicing
print(grocery[1:4])
print(grocery[::2])
print(grocery[::-1])
# above slicing reverses the list but  never use -2,-3 or any -ve value except -1
print(len(numbers))
# len() gives length of list
print(max(numbers))
# max() gives maximum value in list
print(min(numbers))
# min() gives minimum valued element of list
numbers.append(78)
# .append() function adds value at last of the list
numbers.insert(3, 80)
# function .insert() inserts a new number
numbers.remove(82)
# function .remove() removes a entry
numbers.pop()
# function .pop() removes the last entry from list
print(numbers)
numbers[1] = 65
# Mutable means can change
# Immutable means cannot change
tp = (1, 2, 3)  # This is the format of tuple written inside a ()
# This is called a tuple
print(tp)
# tp[1] = 8 this tp is immutable as tp is a tuple
# Lists are mutable whereas Tuples are immutable
Your_Tuple = (45, 56, 62)
# program to swap a number
a = 1
b = 3
temp = a
a = b
b = temp
print(a, b)
# OR   shortcut method
a, b = b, a
print(a, b)