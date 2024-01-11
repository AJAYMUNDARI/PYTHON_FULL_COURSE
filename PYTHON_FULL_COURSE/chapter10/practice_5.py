class train:
    def __init__(self) -> None:
        self.seats = 78
        self.fare=175

    def bookticket(self):
        self.seats= self.seats-1

    def getstatus(self):
        print(self.seats)

    def getinfo(self):
        print(self.fare)

tr=train()
train.getinfo(tr)
train.getstatus(tr)
train.bookticket(tr)
train.getstatus(tr)
        