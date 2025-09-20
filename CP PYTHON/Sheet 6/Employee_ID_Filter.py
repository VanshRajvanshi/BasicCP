n=int(input())
id=list(map(int,input().split()))
x=-1
for i in id:
    if i%2==0:
        print(i,end=" ")
        x=1
if x==-1:
    print(x)