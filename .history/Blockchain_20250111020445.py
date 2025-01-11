from Block import Block

import uuid


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis()]




    def display_chain(self):
        for block in self.chain:
            print(block.__dict__)
            print()


    def create_genesis(self):
        genesis = Block(0,"0","Genesis")
        return genesis
        
    def add_block(self, transaction):
        id = str(uuid.uuid4())
        previous_hash = self.chain[-1].hash
        new_block = Block(id=id,previous_hash=previous_hash,transaction=transaction)
        self.chain.append(new_block)
        print(f"Block adicionado")

    def valid_chain(self):
        for id in range(1,len(self.chain)):
            block = self.chain[id]
            prev_block = self.chain[id - 1]

            if block.hash != block.create_hash():
                return False
            
            if prev_block.hash != block.previous_hash:
                return False
            
        return True



if __name__ == "__main__":
    myBlockchain = Blockchain()

    myBlockchain.display_chain()

    