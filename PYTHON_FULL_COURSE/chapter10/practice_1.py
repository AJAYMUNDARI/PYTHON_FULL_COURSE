class programmer:
    def __init__(self,name,language):
        self.name=name
        self.language=language

    def hum(self):
        print(f"your name is {self.name}")
        return self.language

ajay=programmer("joy","python")
jay=programmer("jimmy","java")

programmer.hum(jay)        #class.func(object) , 
#print(jay.name)            #object._init_ attribute , we calling a attribute of class
print(jay.hum())
print(ajay.hum())            #should return something , we calling a function
