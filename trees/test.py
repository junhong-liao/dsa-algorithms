from treenode import TreeNode
from tree_operations import TreeOperations

# whitespace for code to test binary tree functions

root = TreeNode(1, TreeNode(2), TreeNode(3))
TreeOperationsTester = TreeOperations()
res = TreeOperationsTester.invert(root)
# res = TreeOperationsTester.height(root)
# print(res)
# test = TreeOperationsTester.buildTree(...)
TreeOperationsTester.printTree(res)