# Task 2: Blockchain Workflow Simulation
# Simulate the creation and validation of a block in the blockchain:
# 1. Create multiple transactions, hash them, and build a Merkle tree to obtain the
# Merkle Root.
# 2. Use the Merkle Root, along with the block creation time and the hash of the previous block, to construct a new block.
# 3. Validate the block by using the hash of the previous block to ensure the chain's integrity.
# 4. Simulate adding the block to the blockchain.

import hashlib

class MerkleNode:
    def __init__(self, left=None, right=None, hash_value=None):
        self.left = left 
        self.right = right 
        self.hash_value = hash_value 

class MerkleTree:
    def __init__(self, transactions):
        self.transactions = transactions  
        self.root = None  

    @staticmethod
    def hash(data):
        return hashlib.sha256(data.encode('utf-8')).hexdigest()

    def build_tree(self):
        if not self.transactions:
            return None
        
        leaves = [MerkleNode(hash_value=self.hash(tx)) for tx in self.transactions]

        while len(leaves) > 1:
            if len(leaves) % 2 != 0:
                leaves.append(leaves[-1])

            new_leaves = []
            for i in range(0, len(leaves), 2):
                combined_hash = self.hash(leaves[i].hash_value + leaves[i + 1].hash_value)
                parent_node = MerkleNode(left=leaves[i], right=leaves[i + 1], hash_value=combined_hash)
                new_leaves.append(parent_node)
            
            leaves = new_leaves

        self.root = leaves[0]  

    def get_merkle_root(self):
        return self.root.hash_value if self.root else None
    
    def print_tree(self, node=None, level=0):
        # recursive print
        if node is None:
            node = self.root
        
        if node is not None:
            if node.right is not None:
                self.print_tree(node.right, level + 1)
            
            print(" " * 4 * level + f"Hash: {node.hash_value}")
            
            if node.left is not None:
                self.print_tree(node.left, level + 1)