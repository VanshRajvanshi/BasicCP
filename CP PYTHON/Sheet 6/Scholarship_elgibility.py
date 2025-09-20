n=int(input())
c=0

for i in range(n):
    m,a=map(int,input().split())
    if a>=80 and m>=75:
        c+=1
print(c)