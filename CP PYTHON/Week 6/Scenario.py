n=int(input())
count_pass=0
count_fail=0

mrks=list(map(int,input().split()))

for i in mrks:
    if i>=35:
        count_pass+=1
    else:
        count_fail+=1

print(count_pass," ",count_fail)