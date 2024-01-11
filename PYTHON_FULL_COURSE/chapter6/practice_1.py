#greatest num
a=int(input("enter the number "))
b=int(input("enter the number "))
c=int(input("enter the number "))
d=int(input("enter the number "))
if(a>b):
    great=a
else:
    great=b
if(c>d):
    great2=c
else:
    great2=d
if(great>great2):
    greater=great
else:
    greater=great2
print("greatest num is ",greater)