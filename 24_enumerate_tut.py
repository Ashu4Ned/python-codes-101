l1 = ["potato", "tomato", "okra", "carrot", "ramen", "chopsticks"]

# i = 1
# for item in l1:
#     if i % 2 is not 0:
#         print(f"jarvis please buy these {item}")
#     i += 1

for index, item in enumerate(l1):
    if index % 2 == 0:
        print("jarvis please buy",item, end=",")
