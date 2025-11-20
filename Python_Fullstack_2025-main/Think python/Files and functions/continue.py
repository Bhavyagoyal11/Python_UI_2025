N=int(input("enter a number:"))
for i in range(1,11):
    if((i%2)==0):
        continue
    print(f"{N} x {i} = {N*i}")
    