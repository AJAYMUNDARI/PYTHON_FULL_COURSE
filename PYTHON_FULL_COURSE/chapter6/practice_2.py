#wheather a student is pass or fail
m1=int(input("enter mark "))
m2=int(input("enter mark "))
m3=int(input("enter mark "))
sum=m1+m2+m3
if(sum>=120):
    if(m1>32 and m2>32 and m3>32):
        print("you are pass")
else:
    print("sorry, you are fail")