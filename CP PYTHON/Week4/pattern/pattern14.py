n=int(input("Enter the number:"))
x=1
for i in range(n):
    for j in range(i):
        print(x,end=" ")
        x+=1
    print()
    