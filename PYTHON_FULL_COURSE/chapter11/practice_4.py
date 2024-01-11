class complex:
    def __init__(self,a,b) -> None:
        self.a=a
        self.b=b

    def __add__(self,obj):
        return complex(self.a+obj.a,(self.b+obj.b))
    
    def __mul__(self,obj):
        return complex(self.a*obj.a,(self.b*obj.b))
    
c1=complex(4,5)
c2=complex(5,6)
c3=c1+c2
print(c3.a,c3.b)
c4=c1*c2
print(c4.a,c4.b)
