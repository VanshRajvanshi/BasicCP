a=int(input("Enter a number "))
rev=0
temp=a
while a>0:
    rev=rev*10 + a%10
    a//=10
if rev==temp:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")