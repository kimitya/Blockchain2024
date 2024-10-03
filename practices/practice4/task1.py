# Task 1: Merkle Tree Implementation
# You are required to programmatically implement a Merkle tree using the following steps:
# 1. Represent transactions as hashes (using SHA-256).
# 2. Implement an algorithm that takes a set of transaction hashes and builds a
# binary Merkle tree.
# 3. Your final output should be the Merkle Root, which is the single hash representing all transactions.

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


transactions = ['tx1', 'tx2', 'tx3', 'tx4']  
merkle_tree = MerkleTree(transactions)
merkle_tree.build_tree()
print("Merkle Root:", merkle_tree.get_merkle_root())
print("\nMerkle Tree Structure:")
merkle_tree.print_tree()
