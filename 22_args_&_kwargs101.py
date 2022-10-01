def function_name_print(a, b, c, d):
    print(a, b, c, d)


def funargs(text, *args, **kwargs):
    print(text)
    for item in args:
        print(item)
    for key, value in kwargs.items():
        print(f"{key} is a {value}")


# function_name_print("Hari", "rohit", "shivam", "sun")
# but this can't take more than 4 values this is a major demerit
# to enter more values  we use *args

k = "these are the names"
list_1 = ["Hari", "rohit", "shivam", "sun", "Satyam", "sundar", "naren"]
kw = {"a": "w", "b": "q", "c": "z"}
funargs(k, *list_1, **kw)
