import hashlib
import time


class Block:
    def __init__(self,id,previous_hash, transaction, timestamp = None):
        self.id = id
        self.previous_hash = previous_hash
        self.transaction = transaction
        self.timestamp = time.time()

    def __hash__(self):
        return hash((self.id,self.previous_hash, self.transaction, self.timestamp))
    
    def create_hash(self):
        block_string = f"{self.id}{self.previous_hash}{self.transactions}{self.timestamp}"
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
    print(new_block.__hash__())
    print(new_block.create_hash())
