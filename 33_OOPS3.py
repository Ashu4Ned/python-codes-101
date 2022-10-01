class Employee:
    no_of_leaves = 8,

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def print_details(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"


harry = Employee("Harry Potter", 4500, "born with magical power the hero")
ron = Employee("Ron Weasley", 450, "wizard1")

# harry.name = "Harry Potter"
# harry.salary = 4500
# harry.role = "born with magical power the hero"
#
# ron.name = "Ron Weasley"
# ron.salary = 4500
# ron.role = "wizard1"
# print(ron.__dict__)

print(harry.print_details())
print(ron.print_details())
