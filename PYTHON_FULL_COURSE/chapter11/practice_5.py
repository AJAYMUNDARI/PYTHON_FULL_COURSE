class vector:
    def __init__(self,l1) -> None:
        self.dim=len(l1)
        self.data=l1

    def __add__(self,ob):
        #mylist=ob.data + self.data
        mylist=[]       #make a empty list
        for i in range(len(ob.data)):
            mylist.append(ob.data[i]+self.data[i])
        return vector(mylist)
    
    def __mul__(self,ob):
        dot=0
        for i in range(len(ob.data)):
            dot+=(ob.data[i]+self.data[i])
        return dot
    
v1=vector([8,4,9])
v2=vector([2,6,3])
v=v1+v2
v3=v1*v2
print(v.data)
print(v3)               #__mul__ for vector quantity


#print(v.a,v.b)
#print(len(v1))
#print(len(v2))

