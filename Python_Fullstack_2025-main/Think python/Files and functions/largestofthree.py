num1=int(input("enter number 1:"))
num2=int(input("enter number 2:"))
num3=int(input("enter number 3:"))
def largest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>c):
        return b
    else:
        return c
large=largest(num1,num2,num3)
print(large)
        