# 12 sept 25

# sets
# set can have different data types
dataA = {1, 2, 3, 45, 5.66, "bhavya", True, 1}
print(dataA)
print(type(dataA))
print(id(dataA))
# repeated elements show up only ones
# sets are mutable as well
dataA.add("Riya")
print(dataA)
print(id(dataA))

# empty set
emptySet = set()
print(type(emptySet))

# now if we want to copy dataA data to dataB without using any method
dataB = dataA
print(dataB)

# if we want to copy with a method
dataC = dataA.copy()
print(dataC)
print(id(dataC))
print(id(dataA))
print(id(dataB))

# dataA and dataB have same id , while dataC will have different id


# other set methods
s1 = {1, 2, 3, 4, "bhavya"}
s2 = {3, 5, 6, 7, "goyal"}
s1.add("hello")  # can add one at a time
print(s1)

# to add multiple elements at a time
s1.update([88, 99])
print(s1)

c = s1.intersection(s2)  # common elements
print(c)

d = s1.union(s2)  # all elements (non-repetetive)
print(d)


s1.remove(3)  # throws error if  3 not found
print(s1)

s1.discard(3)  # no error if 3 not found
print(s1)

s1.pop()  # it don't take arguments , and will remove a random element
print(s1)

s2.clear()  # makes the set empty
print(s2)

h = s1.difference(s2)  # will remove common elements from s1 but not from s2
print(h)

s2.update([2, 4, 99, 77])

i = s1.symmetric_difference(s2)
print(i)  # will print uncommon elements of both sets
# both the sets will remain intact
print(s1)
print(s2)

s3 = {2, 4, 99, 88}
b1 = s1.issubset(s3)  # is s1 a subset of s3
print(b1)
b2 = s1.issuperset(s3)  # is s1 a superset of s3
print(b2)

b3 = s2.isdisjoint(s3)  # returns true if both sets have nothing common
print(b3)
# but s2 and s3 have 99 as a common element
