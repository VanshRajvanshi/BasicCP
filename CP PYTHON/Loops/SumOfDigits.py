n=int(input("Enter a number"))
temp=n
sum=0
while temp > 0:
    
    x=temp % 10
    sum = sum + x
    temp //=10
print("Sum:",sum)