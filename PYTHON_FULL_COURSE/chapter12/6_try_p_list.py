#list comprehension
l1=[1,2,3,4,5,6]

#l2=[]
#for item in l1:
   # l2.append(item*item)
l2=[i*i for i in l1 if i>2]
l3=[i*i for i in l1]
print(l2)
print(l3)