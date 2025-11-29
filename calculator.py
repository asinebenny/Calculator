#Calculator program
while True:
    print("Choose your operator")
    print("Choose 1 for +")
    print("Choose 2 for -")
    print("Choose 3 for *")
    print("Choose 4 for /")
    print("Choose 5 to exit")
    #asking the operation to perform
    ch=int(input("Enter your choice"))
    #preventing errors from invalid choices
    if (ch not in [1,2,3,4,5]):
        print("invalid input")
        continue
    #exits the program
    if(ch==5):
        break
    a=float(input("Enter your first number"))
    b=float(input("Enter your second number"))
    if (ch==1):
        print("Your answer is:",a+b)
    elif (ch==2):
        print("Your answer is:",a-b)
    elif (ch==3):
        print("Your answer is:",a*b)
    elif (ch==4):
        if(b==0):
            #prevents division by zero
            print("a number cannot be divided by zero")
        else:
            print("Your answer is:",a/b)