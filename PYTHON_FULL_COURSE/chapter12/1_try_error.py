#built-in exception which are raised when something goes wrong

try:
    print("hello world")
    a=int(input("enter a number: "))
    b=int(input("enter another number: "))
    print(a/b)
    if b>199:
        raise Exception("this number is too large")    #raise Exception

except ValueError:         #any value errorr occur in try box, VE box executed 
    print("value error occured")

except ZeroDivisionError:
    print("This is zero division order")

except Exception in e:                  #all other exception are handled here
    print(f"this problem occur: {e}")  
    
else:                                   #else is not related to if case it related to try case
    print("try was succesful")

print("there were no error")  #cod3 flow continues without program interruption, when exception handled