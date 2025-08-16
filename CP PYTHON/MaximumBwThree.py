a=float(input("Enter a number: "))
b=float(input("Enter a number: "))
c=float(input("Enter a number: "))
if a > b and a > c:
    print(a,"is the greatest number")
elif b > c:
    print(b,"is the greatest number")
else:
    print(c,"is the greatest number")