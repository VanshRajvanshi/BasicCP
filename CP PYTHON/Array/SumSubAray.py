#Given a array find the sum of all subarrays sum
def sum_of_subarrays(arr):
    N=len(arr)
    sum=0
    for i in range(N):
        s=0
        for j in range(i,N):
            s+=arr[j]
            sum+=s
    return sum
A=list(map(int,input().split()))
print(sum_of_subarrays(A))

#If we know in how many subarrays an element is coming we can solve this problem faster
#In how many subarrays index 3 is present
#total=(i+1)*(N-i)