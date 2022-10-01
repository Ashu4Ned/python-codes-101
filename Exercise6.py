# to create snake, water, gun game
import random

choice_list = ["snake", "water", "gun"]
a = random.choice(choice_list)
b = str(input("Enter snake water or gun"))
for choice_list[0] in a:
    if b == "water":
        print("Snake drinks Water, you lose")
    elif b == "gun":
        print("Gun kills Snake, you win")
    else:
        print("TIE")
for choice_list[1] in a:
    if b == "snake":
        print("Snake drinks Water, you win")
    elif b == "gun":
        print("Gun sinks in Water, you lose")
    else:
        print("TIE")
for choice_list[2] in a:
    if b == "snake":
        print("Gun kills Snake, you lose")
    elif b == "water":
        print("Gun sinks in Water, you win")
    else:
        print("TIE")