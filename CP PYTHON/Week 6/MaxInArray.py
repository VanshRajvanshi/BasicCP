arr=list(map(int,input().split()))

max=arr[0]

for i in range(1,len(arr)):
    if arr[i] > max: 
        max=arr[i]
print(max)

ans=-float('inf') 
for i in arr:
    if (ans < i):
        ans=i
print(ans)