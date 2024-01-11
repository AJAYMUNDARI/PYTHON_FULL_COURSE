#dunder method
class Employee:
    def __init__(self,a,name) -> None:   #constructor
        self.a=a
        self.name=name

    def __mul__(self,obj):  #linked to constructor
        return self.a*obj.a
    
    def __str__(obj):       #linked to constructor
        return obj.name 
    
    def __len__(obj):       #linked to constructor
        return obj.a
    
b=Employee(5,"raj")
c=Employee(2,"devraj")
print(b*c)                  #mul dunder method for scalar quantity
#v=b*c
#print(v)                    #mul dunder method for vector quantity
print(b,c)                  #str dunder method
print(len(b))
print(len(c))

