#multiple inheritance
class parents1:
    a=4
    
class parents2:
    b=3
class child(parents1,parents2):
    c=2

h=child()
print(h.a)
print(h.b)
print(h.c)


#multilevel inheritance
class par:
    m=7
    
class chld1(par):
    n=4
    
class chld2(chld1):
    p=8
    
h=chld2()
print(h.m)
print(h.n)
print(h.p)

#super()
class parent:
    e=7
    def __init__(self) -> None:
        print("parent")

class child1(parent):
    f=4
    def __init__(self) -> None:
        super().__init__()          #call constructor of the base class
        print("child1")

class child2(child1):
    g=8
    def __init__(self) -> None:
        super().__init__()
        print("child2")

h=child2()
print(h.e)
print(h.f)
print(h.g)


