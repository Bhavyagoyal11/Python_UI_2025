# Bhavya Goyal
# date - 22 August 2025

print("hello world")

'''
 different data types in python
'''
a = 34  # datatype - int
b = 34.55  # datatype - float
c = True  # datatype - boolean
d = "d"  # datatype - char
e = "hello"  # datatype - string (not a primitive data type of python)

print(a)
print(b)
print(c)
print(d)
print(e)

'''
fstring --(formatted string literal) -- used to embed python expressions directly inside string literals
'''

age = 20
name = "yash"
print(f"Hi my name is {name} and I am {age} years old")


'''
 mutable and immuatable data in python 
'''

# list , sets and dictionaries are example of mutable data type in python
list1 = [1,2,3,4]
print(id(list1)) #id() function prints the memory location where the variable is stored
list1.append(5) # now 5 is added to the list 
print(id(list1))
# since the id before and after making changes in list is same , so list is a mutable data type

set1 = {1,3,4,5,6}
print(id(set1))
set1.add(2) # 2 is added to set1
print(id(set1))
# since the id before and after making changes in set is same , so set is also a mutable data type

#similarly , dictionaries
student = {'name' : 'yash', 'age' : 20 , 'course' : 'B.tect'}
print(id(student))
student['age'] = 19 #value for age is updated 
print(id(student))

'''
immuatable data types are - int , float , string , tuple
'''

a = 22 # a is an integer
print(id(a))
a = a+1
print(id(a))
# different ids before and after changing value of a implies that this data type is immuatable

b = 34.32 # b is an float
print(id(b))
b = b-1
print(id(b))
# different ids before and after changing value of b implies that this data type is immuatable

c = "Yash" #c is an string
print(id(c))
c = c.upper() # for uppercase 
print(id(c))
# different ids before and after changing value of c implies that this data type is immuatable

