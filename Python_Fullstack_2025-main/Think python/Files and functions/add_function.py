def Add(a,b):
    print(a+b)
    
Data=Add(4,5)
print(Data)
 
def sum(a,b):
     return a+b
data=sum(4,5)
print(data)

def sum(a=1,b=2):
    return a+b
print(sum())
print(sum(4))