#star pattern
n=int(input("enter number "))
for i in range(0,n):
    j=n-i-1
    print((" ")*(i),end="")
    print("*"*(2*j+1),end="")
    print((" ")*i)

    