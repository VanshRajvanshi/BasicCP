n = int(input())
car_no=[]


for _ in range(n):
    car_no.append(input())


for carno in car_no:
    even_sum = 0
    odd_sum = 0
    for digit in carno:
        d = int(digit)
        if d % 2 == 0:
            even_sum += d
        else:
            odd_sum += d

    if even_sum % 4 == 0 or odd_sum % 3 == 0:
        print("Yes")
    else:
        print("No")