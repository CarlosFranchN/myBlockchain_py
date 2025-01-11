from Block import Block
import time


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis()]
        self.id = 1

    def __str__(self):
        for block in self.chain:
            print(block)
    def create_genesis(self):
        genesis = Block(0,"0","Genesis")
        return genesis
        
    def add_block(self, transaction):
        id = self.id + 1
        previous_hash = self.chain[-1].create_hash()
        new_block = Block(id=id,previous_hash=previous_hash,transaction=transaction)
        self.chain.append(new_block)
        print(f"Block adicionado")


if __name__ == "__main__":
    myBlockchain = Blockchain()

    print(myBlockchain.chain)

    