A=list(map(int,input().split()))
B=int(input())
arr=[]
for i in range(len(A)):
    arr.append(A[i]+B)    
print(arr)