# Bhavya Goyal
# python file
# dictionaries

# dict = { key : value} pair

data = {"name": "bhavya", "age": 20, list: [1, 3, 4, 5, 6], True: 1, 0: False}
print(data)
# True is assumed to be 1 by default
# value can be mutable as well as immutable , but key should always be immutable , else "unhashable type" error

dict = {"name": "bhavya", "city": "hyd", "age": 20}
for a, b in dict.items():
    print(a, b)
print("done...........")
# here we used .items method , to access both key and value

for key in dict:
    print(key)
print("done...........")
# it will only print keys

for i in dict:
    print(i, dict[i])
print("done...........")
# print(dict["name"]) , this will throw the "keyError"
# here a will assume the values of key and b will assume the values of values

dict.get("name")  # dictionary.get("key")
print("done.............")
# if we try to access a key in a dictionary which does not exists (using get method) , we will get "none"


print(dict.items())
print("done..............")



# updating values
dict["name"] = "yashvardhan"
print(dict["name"])
# dictionaryName[keyName] ---> this is how we access any key in dictionary


# adding another key
dict["course"] = "B.tech"
print(dict.items())




# dictionary methods
# get method
my_dict = {"a": 1, "b": 2, "c": 34.5}
my_dict.get("b")


# my_dict.clear() # clears the whole dictionary
# del deletes the key value pair specified
del my_dict["a"]
print(my_dict)

# len method
print(len(my_dict))

# type method
print(type("c"))

# update
my_dict.update({"b": "yash"})
print(my_dict)

# pop
my_dict.pop("b")

# popItem
# remove and returns the last added item
my_dict.popitem()

# clear , clears the whole dict
my_dict["a"] = 23
my_dict.clear()
print(my_dict)

# keys() , returns the list of the keys
dict1 = {"a": 1, "b": 2}
print(dict1.keys())

# values() , returns the list of the values
print((dict1.values()))




# another way to create a dictionary
# we have to create a list of tuples
data = dict([("name", "yash"), ("age", 20), ("city", "jaipur")])
print(data)
print(type(data))

EmtDict = {}
print(type(EmtDict))

