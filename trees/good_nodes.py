from typing import Optional
from tree_node import TreeNode
from build_tree import TreeBuilder

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = [0]
        def dfs(root: Optional[TreeNode], currentMax: int = float('-inf')) -> None:
            if not root: return
            if root.val >= currentMax: res[0] += 1
            currentMax = max(currentMax, root.val)
            dfs(root.left, currentMax)
            dfs(root.right, currentMax)
        dfs(root)
        return res[0]
    
nodes = [-1, 5, -2, 4, 4, 2, -2, None, None, -4, None, -2, 3, None, -2, 0, None, -1, None, -3, None, -4, -3, 3, None, None, None, None, None, None, None, 3, -3]
tb = TreeBuilder()
root = tb.buildTree(nodes)
s = Solution()
print(s.goodNodes(root))