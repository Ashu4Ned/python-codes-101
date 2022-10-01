def print_new(string):
    return f"return this {string} string to user"


def add(num1, num2):
    return num1 + num2 + 5


# let's test the above functions
# But the catch is this test thing will also be executed in output wherever tut_main1 will be imported
# So to avoid that kinda error we use main

if __name__ == '__main__':
    print(print_new("(this)"))

    o = add(4, 6)
    print(o)
