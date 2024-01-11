try:
    a=int(input("enter a number: "))
    b=int(input("enter another number: "))
    print(a/b)
    if b!=0:
        raise Exception("this is zerodivision order")
    
except ZeroDivisionError:
    print("infinite")

