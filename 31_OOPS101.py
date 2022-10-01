# Classes are like template or blueprint
# and objects are instances of the class
class student:
    pass


Harry = student()
Larry = student()

Harry.name = "Harry Potter"
Harry.std = 10
Harry.section = "Griffindore"

Larry.subjects = ["physics", "Maths"]
Larry.std = 12
print(Harry.name, "\n", Larry.subjects)
