#A SIMPLE BASIC CLASS______________________________
class Employee:
    name="Mosee"
    school="jnv"

ajay=Employee               #object installation, which allow us to allocate the class atrribute

print(ajay.school)
print(Employee.school)      #upto this school atrribute remain same

ajay.school="RRR"           #instance attribute take first preference over class attributes
print(ajay.school)          #print(ajay.school)=print(Employee.school) both are same

Employee.state="odisha"     #ajay.state="odisha" both are same, we add a new atrribute in Employee class
print(ajay.state)           #print(ajay.state)=print(Employee.state) both are same

     
