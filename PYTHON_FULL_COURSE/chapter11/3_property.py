class Employee:
    a=1
    b=4
    c=7
    @classmethod     #class method bound to class not to the object
    def attrr(cls,a,b,c):
        cls.a=a
        cls.b=b
        cls.c=c

    @property        #@property decorator bound to object of class
    def pert(self):  #pert is a method within this @classmethod, not a attribute
        return self.a
    
    @pert.setter     #genrate instance value
    def pert(self,value):
        self.a=value

emp=Employee()
emp.attrr(2,5,8)    #bound to class not to the object of the class, @classmethod
print(emp.pert)     #bound to object of class, @property decorator

emp.pert=56         #we can't do this with setter becuse pert is a method not a attribute
print(emp.pert)

# @getter method: If a func define with @property 
# @setter method: If func define with @name.setter
