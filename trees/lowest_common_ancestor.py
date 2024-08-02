from tree_node import TreeNode

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root: return
        left = None if not root.left else root.left.val
        right = None if not root.right else root.right.val
        if {root.val, left} == {p, q}: return {root.val, left}
        if {root.val, right} == {p, q}: return {root.val, right}
        if {left, right} == {p, q}: return {left, right}
        self.lowestCommonAncestor(root.left)
        self.lowestCommonAncestor(root.right)

