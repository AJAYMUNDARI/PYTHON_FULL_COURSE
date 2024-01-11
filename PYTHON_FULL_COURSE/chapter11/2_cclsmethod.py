class Employee:
    a=1
    b=4
    c=7
    @classmethod
    def attrr(cls,a,b,c):
        cls.a=a
        cls.b=b
        cls.c=c

emp=Employee()
print(Employee.a)
print(Employee.b)
print(Employee.c)
emp.attrr(2,5,8)
print(Employee.a)
print(Employee.b)
print(Employee.c)