a=float(input("Enter 1st angle"))
b=float(input("Enter 2nd angle"))
c=float(input("Enter 3rd angle"))
if a + b + c != 180:
    print("Not a valid triangle")
else:

    if a==90 or b==90 or c==90:
        print("It is a right angle triangle")
    elif a<90 or b<90 or c<90:
        print("It is a acute angle triangle")
    else:
        ("It is a obtuse angle triangle")
        