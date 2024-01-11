class animal:
    def __init__(self) -> None:
        pass

class pets(animal):
    def __init__(self) -> None:
        super().__init__()
        print("pets")

class dog(pets):
    def __init__(self,name) -> None:
        self.name=name
        super().__init__()

    def bark(self):
        print(f"{self.name}")

a1=dog("baooo baooo")
a1.bark()
