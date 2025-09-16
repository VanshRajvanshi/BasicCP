N=int(input("Enter the length of the list:"))
arr=[]
for i in range(N):
    arr.append(int(input("Enter the element:")))

max=arr[0]
min=arr[0]

for i in arr:
    if i>max:
        max=i
    if i<min:
        min=i
print("Maximum: ",max)
print("Minimum: ",min)