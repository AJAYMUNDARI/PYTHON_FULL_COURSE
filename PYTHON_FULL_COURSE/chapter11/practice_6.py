class complex:
    def __init__(self,i,j,k) -> None:
        self.i=i
        self.j=j
        self.k=k
    #case 1
    def __str__(self):
        return f"{self.i}i+{self.j}j+{self.k}k"


    #case 2
    def dimen(self):
        print(f"{self.i}i+{self.j}j+{self.k}k")

c=complex(7,8,10)       #for case 1, where we use __str__ func and print the output  
print(c)

x=complex(7,8,10)       #for case 2, where we need to call the function and get the output
x.dimen()