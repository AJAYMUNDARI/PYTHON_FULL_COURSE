class Employee:
    def __init__(self,salary,increment) -> None:
        self.salary=salary
        self.increment=increment
        
    @property
    def salaryafterincrement(self):
        return self.salary * (1+self.increment)
    
emp1=Employee(1000,.1)
print(emp1.salaryafterincrement)
