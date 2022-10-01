# i = 0
# while (i < 45):
#     print(i+1, end=" ")
#     i = i + 1

#  this is a finite while loop, For an infinite loop
#
# j = 0
# while(True):
#     if j + 1 < 5:
#         j = j + 1
#         continue
#     print(j+1, end=" ")
#     if(j == 44):
#         break # stop the loop
#     j = j+1

while (True):
    k = int(input("Enter a number"))
    if k > 100:
        print("congrats! you have entered correct value greater than 100")
        break
    else:
        print("Try again!\n")
        continue
