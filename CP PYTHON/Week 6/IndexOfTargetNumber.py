arr=list(map(int,input().split()))
target =int(input())
index=0
for i in range(len(arr)):
    if arr[i]==target:
        index=i
        break
print(index)

#1 2 3 3  4
