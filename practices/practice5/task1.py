import hashlib
import time

class Block:
    def __init__(self, block_number, transactions, previous_hash=""):
        self.block_number = block_number
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = None
        self.hash_value = None

def mine_block(block, target_zeros):
    nonce = 0
    start_time = time.time()
    target = "0" * target_zeros  

    while True:
        text = f"{block.block_number}{block.transactions}{block.previous_hash}{nonce}"
        hash_value = hashlib.sha256(text.encode('utf-8')).hexdigest()
        
        if hash_value.startswith(target):
            end_time = time.time()
            block.nonce = nonce
            block.hash_value = hash_value
            return nonce, hash_value, end_time - start_time
        
        block2=Block(block.block_number+1, block.transactions, hash_value)
        print(f"Block mined:\n Number: {block2.block_number}\n Hash Value: {block2.previous_hash}\n ")
        block=block2
        nonce += 1


target_zeros = 5  

block1 = Block(block_number=58, transactions="tr4", previous_hash="")
nonce1, hash_value1, elapsed_time1 = mine_block(block1, target_zeros)

print(f"End block mined:\nHash Value: {hash_value1}\nNonce: {nonce1}\nTime taken: {elapsed_time1:.2f} seconds\n")
