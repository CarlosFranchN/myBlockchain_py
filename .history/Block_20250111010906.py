import hashlib
import time


class Block:
    def __init__(self,id,previous_hash, transaction, timestamp = None):
        self.id = id
        self.previous_hash = previous_hash
        self.transaction = transaction
        self.timestamp = time.time()
        self.hash = self.create_hash()

    
    def create_hash(self):
        # return self.__dict__
        block_string = f"{self.__dict__}"
        # f"{self.id}{self.previous_hash}{self.transaction}{self.timestamp}"
        return hashlib.sha256(block_string.encode()).hexdigest()





if __name__ == "__main__":
        # Supondo que temos o seguinte bloco anterior
    previous_block_hash = "abc123"  # Este seria o hash do bloco anterior na blockchain

    # Transação de exemplo
    transaction = "Carlos enviou 10 BTC para Maria"

    # Criando uma instância do Block
    new_block = Block(id=1, previous_hash=previous_block_hash, transaction=transaction)

    # Visualizando os atributos do novo bloco
    print(f"ID do Bloco: {new_block.id}")
    print(f"Hash do Bloco Anterior: {new_block.previous_hash}")
    print(f"Transação: {new_block.transaction}")
    print(f"Timestamp: {new_block.timestamp}")
    print(new_block.hash)
