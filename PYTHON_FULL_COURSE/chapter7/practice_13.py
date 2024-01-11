num=7
factorial = 1
i=1
if num<0:
    print("factorial not possible")
elif num == 0:
    print("factorial of 0 is 1")
else:
    while i < num+1:
        factorial *=i
        i+=1
    print("factorial of",num,"is",factorial)
        