class job:
    def __init__(self, name, language):
        self.name= name
        self.language= language
    
    def store (self):
        print(f"your name is {self.name}")
        return self.language
    
aj=job("ajay","java")
bj=job("bijay","python")

job.store(aj)
job.store(bj)

print(aj.store())
print(bj.store())