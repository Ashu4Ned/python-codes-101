new_list = [5, "lane", "chips", "incense", 70, 96, "helm", 45, 32, "large", 'small']
# for items in new_list:
#     if type(items) == int:
#         if items >= 6:
#             print(items)
#     else:
#         print("none")

# OR
for items in new_list:
    if str(items).isnumeric() and items > 6:
        print(items)
