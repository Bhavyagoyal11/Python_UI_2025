# Bhavya Goyal
# 05/09/2025

name = "bhavya goyal" # indexing starts from 0
#strings are immutable
print(name[2])

print(name[3:14:2])
# string[start : end : step] , where end index is not included and n steps means nth index from the current element

text = 'PythonProgramming'
print(text[0:7]) # no step value

text = "pythonprogramming"
print(text[0:7:2]) #  step is set to 2 , means every 2nd element will be printed

text = "programmingpython"
print(text[:7])
print(text[0::2])# now the ending index is not mentioned therefore it will be printed till end having a step of 2

# negative indexing starts with -1 starting from the last element
text = "PythonProgramming"
print(text[-1:])#last character
print(text[:-1]) #everycharacter will be printed excepted last one
print(text[::-1]) # print the whole string in reverse

text = "programming"
print("ing" in text) # memebership operator

print("abcd" not in text) #because "abcd" is not present in the text
print(len(text)) # len function

#tuple
# tuples is an ordered , immutable collection of items
tup = () #empty tuple
print(tup)
tup1 = (4,3,2,1) # tuple with same datatype
tup2 = ("A" , 3, True, 4.22) #tuple with mixed data types
print(id(tup2))
tup2 = (False)
print(id(tup2))

#tuple
# tuples is an ordered , immutable collection of items
tup = () #empty tuple
print(tup)
tup1 = (4,3,2,1) # tuple with same datatype
tup2 = ("A" , 3, True, 4.22) #tuple with mixed data types
print(tup2)
print(id(tup2))
print(tup2[3]) # indexing and accessing element of the tuple
tup2 = (False)
print(tup2)
print(id(tup2))

#since we are getting two different ids for tup2 before and after tup2 = (False)

tup3 = (1,2,3,4,5,('a' ,'b' ,'d'))
print(tup3[5][2]) # first we accessed the 5th element as the inner tuple is at 5th index , then we go for 2nd index inside that for 'd'

#single element tuple
a = (73) # this not a tuple but an integer
print(a)
print(type(a))
a = (73, )# now this is a tuple with a single element
print(a)
print(type(a))

a = (1,2,3,4,5)
b = ('a' , 'b' , 'c')

#tuple concatination
print(a+b)

print(a*3) #tuple repetition
print(a[0]*3) # this will multiply the value with 3 , but not repeate it 3 times inform of comma separated values
print()
#membership
print(2 in a)
print(9 in a)

#immutability
t = (1,2,3,4)
# t[0] = 4  it will give an error because tuples are immutable

data = 3,4,5,6
print(type(data))
#therefore , by default , when we add commas in between , it is treated as a tuple
data2 = 34,
print(type(data2))

print(f"{data} , {data2}")

#tuple methods
tu = (3,2,2,4,6)
print(tu.index(2)) # prints the index of first occurance of

#tuple packing and unpacking
#packing
t = 1 , "python" , 3.14
print(t)
# print(t[0:-1]) #it will print all except last
#unpacking
a , b , c = t
print(a) # 1
print(b) # "python"
print(c) #3.14

t3 = (78 , 3, 4 , 5, 6,"Yash")
print(t3[3:-1]) # 5 , 6
print(t3[3:-3]) # nothing
print(t3[3:0]) # nothing
print(t3[-3:0]) #nothing
print(str(t3[4])*3) #printing an element multiple times by first converting it into string

tuplet = (9,9,9,1,2,2,3,4,5,5,53,23,71,93)
print(tuplet.count(9))

#list is an order,  mutable , indexed collecion of items (diff data structures) in python
list = [1,2,3,4,5]
print(id(list))
list.append(9)
print(id(list))
# the id will be same for both list , therefore , lists are mutable

myList = [1,2,3,4.55 , "yash" , True]
print(myList)

list1 = [1,2,3,4,5,6,78.9 , "yash" , (6,7,"90") , [3,40]]
print(list1[-1][-1])
print(list1[8][1])
print(id(list1))
list1 = [1,2,3,4]
print(list1) # this will have another id , but it does not mean that list is immutable , if we want to check for mutability , we need to mutate using its methods
print(id(list1))

data = [1,2,3,4,5]
print(id(data))
data.append(9)
print(id(data))

# insert index
data2 = [1,2,3,4,5,8]
data2.insert(3,7) # inserts 7 at 3rd index
print(data2)
#remove
data2.remove(7) # removes the element mentioned
print(data2)

#pop
data2.pop() # by default removes the last element
print(data2)
data2.pop(3) # removes the element at 3rd index
print(data2)

#index --> prints the index of a specific item
print(data2.index(2))

#replace ---> replaces
sentence = "I like apples and apples are sweet."
new = sentence.replace("apples" , "mangoes")
print(new)


#clear ---> empty the list
data2.clear()
print(data2)
