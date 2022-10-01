import time

# initial = time.time()
# for i in range(100):
#     print("This is a line")
# print(f"for loop took {time.time()-initial} seconds")

initial2 = time.time()
k = 0
while (k < 100):
    print("this is a line")
    time.sleep(2)
    k += 1
print(f"while loop took {time.time()-initial2} time")

localtime = time.asctime(time.localtime(time.time()))
print(f"local time is, {localtime}")

