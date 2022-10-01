number_of_guesses = 1
print("enter a number between 1 to 100")
print("you have total 9 guesses")
input_number = int(input("Enter the number to guess"))
while (number_of_guesses <= 9):
    if input_number < 45:
        print("your guess is less than original number, please enter higher value.\n")
    elif input_number > 45:
        print("your guess is greater than original number, please enter lower value.\n")
    else:
        print("you won\n")
        print(number_of_guesses, "numbers of guesses you took to guess")
        break
    print(9 - number_of_guesses, "number of guesses you are left with")
    number_of_guesses = number_of_guesses + 1
if (number_of_guesses > 9):
    print("GAME OVER")
