from Block import Block
from Blockchain import Blockchain
from Transaction import Transaction

t1 = Transaction("Carlos","Franch",500)
t2 = Transaction("Carlos","Caldrim",200)
t3 = Transaction("Groot","Rocket",1500)

print(t1)
print(t2)
print(t3)




myBC = Blockchain()
myBC.display_chain()

myBC.add_block(t1)
myBC.add_block(t2)
myBC.add_block(t3)

myBC.display_chain()
