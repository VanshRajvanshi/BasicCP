n=int(input())
d=list(map(int,input().split()))
k=int(input())
c=0
for i in d:
    for j in d:
        if i+j==k and i!=j:
            c+=1
print(c//2)

