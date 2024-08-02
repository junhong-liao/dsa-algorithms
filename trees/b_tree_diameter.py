from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # @staticmethod
    # def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    #     res = [0] # lists: mutable
    #     def dfs(root: Optional[TreeNode]) -> int:
    #         if not root:
    #             return -1
    #         left = dfs(root.left)
    #         right = dfs(root.right)
    #         res[0] = max(res[0], left + right + 2)
    #         return 1 + max(left, right)
    #     dfs(root)
    #     return res[0]
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(root) -> int:
            if not root: return -1
            left, right = dfs(root.left), dfs(root.right)
            self.res = max(self.res, 2 + left + right)
            return 1 + max(left, right)
        dfs(root)
        return self.res
    
node = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
print(Solution.diameterOfBinaryTree(node))



        