
class Transaction:
    def __init__(self,sender,receiver,amout):
        self.sender = sender
        self.receiver = receiver
        self.amout = amout

    def __str__(self):
        return f"{self.sender} -> {self.receiver} : R$ {round(self.amout, 2)}"
        