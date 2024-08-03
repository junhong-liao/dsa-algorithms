'''
from binarytree import build, pprint

# Create a binary tree
nodes = [1, 2, 3, 4, 5, 6, 7]
tree = build(nodes)

# Pretty print the tree
pprint(tree)

TREE VISUALIZER: https://solomk.in/leetcode-tree-visualizer

'''
# binary tree node definition
class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right