def function():
    try:
        print("hello world")
        a=int(input("enter a number: "))
        b=int(input("enter another number: "))
        print(a/b)
        return a/b

    except Exception in e:                  #all other exception are handled here
        print(f"this problem occur: {e}")  
        return 0

    finally:                                #exceuted regardless of error
        print("i will always be excuted")

#to check the status ofmodule                       #__name__ exaluate to the name of the module
print(__name__)         #when program is running from same module __name__==___main__ & when we import the module __name__==__name__
if __name__=='__,main__':   
    function()          #excecute if running from same module
    print("main")       #excecute if running from same module