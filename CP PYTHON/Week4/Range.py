# print(list(range(0, 6))) range is iterable

# for i in range(1,10,2):
#     print(i)

# N=int(input("Enter a number: "))
# for i in range(1,N+1):
#     print(i,end=" ")

# N=int(input("Enter a number: "))
# for i in range(1,N+1,2):
#     print(i,end=" ")

# a=int(input("Enter a number: "))
# b=int(input("Enter a number: "))
# p=1
# for i in range(b):
#     p=p*a
# print("The power is:", p)

a=int(input("Enter a number: "))
for i in range(1, a+1):
    if i%3== 0:
        continue
    print(i, end=" ")