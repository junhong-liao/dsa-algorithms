from tree_node import TreeNode
from typing import Optional

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot = Optional[TreeNode]) -> bool:
        if not root: return False # there will always be a subRoot
        if self.isSameTree(root, subRoot): return True
        return self.isSubTree(root.left, subRoot) or self.isSubTree(root.right, subRoot)

    def isSameTree(self, a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
        if not a and not b: return True # avoided returning false until leafs, means subtree of a and b were identical
        if (not a or not b) or (a.val != b.val): return False
        return self.isSameTree(a.left, b.left) and self.isSameTree(a.right, b.right)