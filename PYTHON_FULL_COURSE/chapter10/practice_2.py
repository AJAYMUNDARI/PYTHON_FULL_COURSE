import math
class calculator:
    def __init__(self,num) -> None:
        self.num=num
    def square(self):
        #print(f"hello{self.num}")
        return self.num * self.num
    
    def cube(self):
        return self.num*self.num*self.num
    
    def root(self):
        return math.sqrt(self.num)
    
ajay=calculator(5)
print(ajay.square())
print(ajay.cube())
print(ajay.root())
calculator.square(ajay)
#calculator.cube(ajay)
#calculator.root(ajay)
