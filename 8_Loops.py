# for loop

list1 = ["hen", "ben", "ken", "men", "lane", "chain"]
tuple1 = (6, 3, 5, 4, 8, 7)
bill = [["Lays", 50], ["Biscuit", "30"], ["Deo", "200"], ["Shampoo", 210]]
k = len(list1)
print(k)
for item in list1:
    print(item)
for nos in tuple1:
    print(nos)
for items in bill:
    print(items)
for product, rate in bill:
    print(product,"and its rate is", rate)
dict1 = dict(bill)
for product, rate in dict1.items():
    print("rate of ", product, " is rs.", rate)

# while loop

i = 0
while (i < 45):
    print(i)
    i = i + 1
