B=int(input("Enter the number: "))
print("Enter array elements: ")
A=list(map(int,input().split()))
N=len(A)
max=0
for i in range(N):
    s=0
    for j in range(i,N):
        s+=A[j]
        if s<=B and s>max:
            max=s
            
print("Number of maximum subarray is ",max)