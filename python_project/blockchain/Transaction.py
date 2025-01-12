
class Transaction:
    def __init__(self,sender,receiver,amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = float(amount)

    def __str__(self):
        return f"{self.sender} -> {self.receiver} : R$ {round(self.amount, 2)}"

    def to_dict(self):
        return {
            'sender': self.sender,
            'receiver': self.receiver,
            'amount': self.amount
        }


if __name__ == "__main__":
    t1 = Transaction("Carlos","Franch",500)
    t2 = Transaction("Carlos","Caldrim",200)
    t3 = Transaction("Groot","Rocket",1500)

    print(t1)
    print(t2)
    print(t3)