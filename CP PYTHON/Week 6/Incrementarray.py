arr=list(map(int,input().split()))

inc=int(input("Enter the increment value: "))

x=[]

for i in range(len(arr)):
    x.append(arr[i]+inc)

print(x)

