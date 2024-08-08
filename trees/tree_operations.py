from typing import Optional, List
from collections import deque
from tree_node import TreeNode

class TreeOperations():

    # build a binary tree for testing purposes
    def buildTree(self, arr: Optional[List[int]], index: int = 0) -> Optional[TreeNode]:
        if index >= len(arr) or not arr[index]: return None
        root = TreeNode(val = arr[index])
        root.left = self.buildTree(arr, 2 * index + 1)
        root.right = self.buildTree(arr, 2 * index + 2)
        return root

    # invert a binary tree
    def invert(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        if not node: return None
        node.left, node.right = self.invert(node.right), self.invert(node.left)
        return node
    
    '''
    find height of a binary tree
    height defined as max edges from root (or target node) to lea
    '''
    def height(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        return 1 + max(self.height(root.left), self.height(root.right))
    
    # returns max depth
    def depth(self, root: Optional[TreeNode]) -> int:
        if not root: return -1
        return 1 + max(self.depth(root.left), self.depth(root.right))

    # calculate max diameter between two TreeNodes
    def diameter(self, root: Optional[TreeNode]) -> int:
        res = 0 # max span, or diameter
        def dfs(root):
            nonlocal res
            if not root: return 0
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left + right)
            return 1 + max(left, right)
        dfs(root)
        return res
    
    # check if a binary tree is balanced
    def isBalanced(self, root: Optional[TreeNode]) -> int:
        res = True
        def dfs(root):
            nonlocal res
            if not root: return 0
            left, right = dfs(root.left), dfs(root.right)
            if abs(left - right) > 1: res = False
            return 1 + max(left, right)
        dfs(root)
        return res

    # check if two binary trees are the same
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        if not p or not q: return False
        if p.val != q.val: return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    # checks the number of "good nodes" in a binary tree
    def goodNodes(self, root: Optional[TreeNode]) -> int:
        res = [0]
        def dfs(root: Optional[TreeNode], currentMax: int = float('-inf')) -> None:
            if not root: return
            if root.val >= currentMax: res[0] += 1
            currentMax = max(currentMax, root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return res[0]



