n=[2,3,4,5,6,8,10]
x=int(input("enter a number:"))
i=0
while(i<7):
    if(n[i]==x):
        print("number found")
        break
    else:
        print("number not found!")
    i+=1