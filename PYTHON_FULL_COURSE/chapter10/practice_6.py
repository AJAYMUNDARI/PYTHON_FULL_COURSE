#self is changed to irctc
class train:
    def __init__(irctc) -> None:  
        irctc.seats = 78
        irctc.fare=175

    def bookticket(irctc):
        irctc.seats= irctc.seats-1

    def getstatus(irctc):
        print(irctc.seats)

    def getinfo(irctc):
        print(irctc.fare)

tr=train()
train.getinfo(tr)
train.getstatus(tr)
train.bookticket(tr)
train.getstatus(tr)
        