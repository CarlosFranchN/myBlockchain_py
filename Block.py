import hashlib
import time
from random import randint


class Block:
    def __init__(self,id,previous_hash, transaction,proof, timestamp = None):
        self.id = id
        self.previous_hash = previous_hash
        self.transaction = transaction
        self.proof = proof
        self.timestamp = time.time()
        self.hash = self.proof_of_work()

    def __str__(self):
        return f"{self.__dict__}"
    
    def create_hash(self):
        block_string = f"{self.__dict__}"
        return hashlib.sha256(block_string.encode()).hexdigest()
    

    def valid_proof(self, hash):
        validate = hash[:4] == "0000"
        return validate

    def proof_of_work(self):
        while True:
            hash = self.create_hash()
            if self.valid_proof(hash):
                return hash
            self.proof+=1





if __name__ == "__main__":
        # Supondo que temos o seguinte bloco anterior
    previous_block_hash = "abc123"  # Este seria o hash do bloco anterior na blockchain

    # Transação de exemplo
    transaction = "Carlos enviou 10 BTC para Maria"
    proof  = 1
    # Criando uma instância do Block
    new_block = Block(id=1, previous_hash=previous_block_hash, transaction=transaction, proof=proof)

    # Visualizando os atributos do novo bloco
    print(f"ID do Bloco: {new_block.id}")
    print(f"Hash do Bloco Anterior: {new_block.previous_hash}")
    print(f"Transação: {new_block.transaction}")
    print(f"Proof: {new_block.proof}")
    print(f"Timestamp: {new_block.timestamp}")
    print(new_block.hash)
    # print(new_block.valid_proof())
