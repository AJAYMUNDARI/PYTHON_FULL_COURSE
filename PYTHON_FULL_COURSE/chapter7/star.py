n=int(input("Enter n:"))
print(" "*(n-1)+"*"+" "*(n-1))
for i in range(1,n-2):
    print(" "*(n-i-1)+"*"+" "*(2*i-1)+"*"+" "*(n-i-1))
print("*"*(2*n-1))