class Employee:
    no_of_leaves = 8
    pass

harry = Employee()
ron = Employee()

harry.name = "Harry Potter"
harry.salary = 4500
harry.role = "born with magical power the hero"

ron.name = "Ron Weasley"
ron.salary = 4500
ron.role = "wizard1"
print(ron.__dict__)

print(ron.name)
print(Employee.no_of_leaves)
ron.no_of_leaves = 13
harry.no_of_leaves = 21 # as he bunks more classes searching for bad people
print(Employee.__dict__)


