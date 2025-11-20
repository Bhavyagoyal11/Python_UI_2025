file=open("./even_odd.py","r")
# if a function returns something then it can be stored in a variable this open function is returning something
print(file.read())
# agar isme integer pass karenge to first three character print ho jayenge
file.close()

file=open("./greet.py","r")
print(file.readline())
file.close()

file=open("./even_odd.py","r")
# if a function returns something then it can be stored in a variable this open function is returning something
print(file.read(3))
# agar isme integer pass karenge to first three character print ho jayenge
file.close()

file=open("./greet.py","r")
print(file.readlines())
# when we use readlines then data come in array
file.close()

# file=open("./even_odd.py","w")
# print(file.write("hello prakhar aditya"))
# file.close()
 
# file=open("./even_odd.py","w")
# print(file.write("dfgafgasf"))
# file.close()
 

# file=open("./even_odd.py","a")
# print(file.write("hello prakhar aditya"))
# file.close()

# to delete a file we must import an os
import os 
os.remove("./delete.py")