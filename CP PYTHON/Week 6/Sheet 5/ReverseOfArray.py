A=list(map(int,input().split()))

rev=[]

for i in range(len(A)-1,-1,-1):
    rev.append(A[i])
print(rev)