a=[1,4,6,'apple']
i=0
#for item in a:
   #i=i+1
   #print(f"item number {i} is {item}")
   
for i, item in enumerate(a):
   print(f"item number {i+1} is {item}")
   
for item in enumerate(a):
   print(f"item number {i+1} is {item}")
