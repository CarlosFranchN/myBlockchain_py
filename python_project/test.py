from blockchain.Block import Block
from blockchain.Blockchain import Blockchain
from blockchain.Transaction import Transaction

t1 = Transaction("Carlos","Franch",500)
t2 = Transaction("Carlos","Caldrim",200)
t3 = Transaction("Groot","Rocket",1500)

print(t1)
print(t2)
print(t3)




myBC = Blockchain()
myBC.display_chain()

myBC.add_block(t1,1)
myBC.add_block(t2,2)
myBC.add_block(t3,3)
print(myBC.get_dict())
# myBC.display_chain()
# print(myBC.valid_chain())

# print(myBC.last_block())

# last_block = myBC.last_block()



