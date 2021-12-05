from Voting import BlockChain

blockchain= BlockChain()

v10 = blockchain.new_transaction("voter1","condidat1",6)
v11 = blockchain.new_transaction("voter1","condidat2",4)
v12 = blockchain.new_transaction("voter1","condidat3",1) 
blockchain.new_block(proof=5555)

v20 = blockchain.new_transaction("voter2","condidat1",1)
v21 = blockchain.new_transaction("voter2","condidat2",4)
v22 = blockchain.new_transaction("voter2","condidat3",6) 
blockchain.new_block(proof=5555)

print("votes",blockchain.chain)