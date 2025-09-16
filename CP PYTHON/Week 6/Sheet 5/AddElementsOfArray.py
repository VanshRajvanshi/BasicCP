A1=list(map(int,input().split()))
A2=list(map(int,input().split()))
A3=[]
for i in range(len(A1)):
    A3.append(A1[i]+A2[i])
print(A3)