class Employee:
    name="Mosee"
    school="jnv"
    #func getsalary() is defined
    def salary(self):             #function for self parameter/instance 
        print(f"{self.name} is your name and u are class atrribute")

    def __init__(self,name,mark): #constructor function for different object having self parameter which execute any funtion according to argument
        self.name=name            #instance attribute/self prameter
        self.mark=mark            #instance attribute

    def getsalary(self):          #function for self parameter/instance 
        print(f"{self.name} is your name")
        print(f"{self.mark} is your mark")

    @staticmethod                 #gender as a static method
    def gender():       
        print("Thank God, It is a static method")

ajay=Employee("raj",55)     #object=class(p1,p2), init funtion require object for each entry
mosee=Employee("nitu",77)   #2
Employee.getsalary(ajay)
Employee.getsalary(mosee)

Employee.gender()                  #ajay.gender() are same, static method doesn't require object to call function

raju=Employee                    #new object for Employee
Employee.salary(raju)             #self parameter, class.function(object)