arr=list(map(int,input().split()))
x=[]
for i in arr:
    if i%2!=0:
        x.append(i)
print(x)