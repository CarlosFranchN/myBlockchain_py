from blockchain.Block import Block
from blockchain.Transaction import Transaction
import json
import uuid
import hashlib



class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis()]





    def display_chain(self):
        for block in self.chain:
            print(block.__dict__)
            print()

    def get_dict(self):
        chain = {}
        key = "#"
        # num_qtd = 1
        for block in self.chain:
            chain[f"{key}{block.id}"] = block.__dict__
            # num_qtd+=1
        return chain


    def create_genesis(self):
        genesis = Block(0,"0",Transaction(sender="Genesis",receiver="Genesis", amount=0),1)
        return genesis
        
    def add_block(self, transaction, proof):
        id = self.last_block().id + 1
        previous_hash = self.chain[-1].hash
        new_block = Block(id=id,previous_hash=previous_hash,transaction=transaction, proof=proof)
        self.chain.append(new_block)
        print(f"Block adicionado")

    def valid_chain(self):
        for id in range(2,len(self.chain)):
            block = self.chain[id].__dict__
            prev_block = self.chain[id - 1].__dict__

            if block['previous_hash'] != prev_block['hash']:
                print(block)
                return False
            
        return True
    def last_block(self):
        return self.chain[-1]
       

    



if __name__ == "__main__":
    myBlockchain = Blockchain()

    myBlockchain.display_chain()

    