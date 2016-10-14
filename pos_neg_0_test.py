test1=1;

while test1 != 0:
    test1=int(input("Please enter a number or to terminate enter 0   "))
    if test1 > 1:
        print("This number is positve")
    elif test1 < 0:
        print("This number is negative")
    else:
        print("This number is zero")
