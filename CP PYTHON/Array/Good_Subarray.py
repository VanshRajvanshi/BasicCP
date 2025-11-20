A=list(map(int,input().split()))
B=int(input("Enter the number: "))
c=0
N=len(A)
for i in range(N):
    s=0
    x=0
    for j in range(i,N):
        s+=A[j]
        x=j-i+1
        if (s<B and x%2==0):
            c+=1
        if (s>B and x%2!=0):
            c+=1
print("Number of good subarrays is ",c)