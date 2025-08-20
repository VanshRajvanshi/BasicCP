n=4
m=4
# i=1
# while (i<=m):
#     print("*",end=" ")
#     i+=1

# for i in range(n+1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

for i in range(n+1):
    for j in range(n-i):
        print("*",end=" ")
    print()
