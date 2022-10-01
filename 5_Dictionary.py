# Dictionary is nothing but key value pairs
d1 = {}
print(type(d1))
d2 = {"a": "1", "b": "2", "c": "3", "d": {"a1": "11", "b2": "22"}}
# This is mapping of one key to other to form key value pairs
""" we can also feed another dictionary for a key value,
like we matched the key d with dictionary
"""
print(d2)
print(d2["c"])
print(d2["d"])
d2["e"] = "5"
print(d2)
d2["z"] = "26"
print(d2)
del d2["z"]
print(d2)
print(d2.copy())
d3 = d2
del d3["a"]
print(d2)
d2.update({"f": "6"})
print(d2)
