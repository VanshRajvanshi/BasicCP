A=list(map(int,input().split()))
diff=0
even_count=0
odd_count=0
for i in A:
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1
diff= abs(even_count-odd_count)
print(diff)