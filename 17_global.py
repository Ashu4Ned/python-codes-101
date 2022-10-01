l = 5
m = 9
# this is global variable can be used throughout syntax
def function1(n):
    l = 3
    global m
    # global keyword is used to access global variable inside local function
    print(l*m)
    print(f"local variable l is {l}")
    # here l is local variable it will only be used inside the function
    print(f"{n * l}  , I have printed")


function1("this is me")
print(f"global variable l is {l}")
