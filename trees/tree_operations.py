from typing import Optional
from collections import deque
from treenode import TreeNode

class TreeOperations():
    # how to override print function?
    # def printTree(self, root: Optional[TreeNode]) -> None:
    #     if not root: return
    #     queue = deque([root])
    #     while queue:
    #         node = queue.popleft()
    #         print(node.val, end='')
    #         if node.left: queue.append(node.left)
    #         if node.right: queue.append(node.right)

    def buildTree(self, nums):
        if not nums:
            return None
        root = TreeNode(nums[0])
        q = [root]
        i = 1
        while i < len(nums):
            curr = q.pop(0)
            if i < len(nums):
                curr.left = TreeNode(nums[i])
                q.append(curr.left)
                i += 1
            if i < len(nums):
                curr.right = TreeNode(nums[i])
                q.append(curr.right)
                i += 1
        return root
 
    def printTree(self, root: Optional[TreeNode]):
        if not root:
            return
        self.printTree(root.left)
        print(root.val, end=" ")
        self.printTree(root.right)

    # invert a binary tree
    def invert(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        if not node: return None
        node.left, node.right = self.invert(node.right), self.invert(node.left)
        return node
    
    # find height of a binary tree
    # height defined as max edges from root (or target node) to leaf
    def height(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        return 1 + max(self.height(root.left), self.height(root.right))
    
    # returns max depth
    def depth(self, root: Optional[TreeNode]) -> int:
        if not root: return -1
        return 1 + max(self.depth(root.left), self.depth(root.right))

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

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        if not p or not q: return False
        if p.val != q.val: return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
