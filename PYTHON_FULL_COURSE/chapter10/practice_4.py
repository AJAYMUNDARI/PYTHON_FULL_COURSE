import math
class calculator:
    def __init__(self,num) -> None:
        self.num=num
    def square(self):
        return self.num * self.num
    
    def cube(self):
        return self.num*self.num*self.num
    
    def root(self):
        return math.sqrt(self.num)
    
    @staticmethod
    def greet():
        print("Hello")
    
ajay=calculator(5)
print(ajay.square())
print(ajay.cube())
print(ajay.root())
calculator.greet()
#calculator.square(ajay)
#calculator.cube(ajay)
#calculator.root(ajay)
