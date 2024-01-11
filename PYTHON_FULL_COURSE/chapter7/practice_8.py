n=int(input("enter number "))
for i in range(0,n):
    j=n-i-1
    print("*"*(i+1),end="")
    print(" "*j)