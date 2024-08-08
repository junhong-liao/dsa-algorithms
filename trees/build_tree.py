from typing import Optional, List
from tree_node import TreeNode

class TreeBuilder:
    def __init__(self):
        ...
    
    def buildTree(self, arr: Optional[List[int]], index: int=0) -> Optional[TreeNode]:
        if index >= len(arr) or arr[index] == None: return None
        root = TreeNode(val=arr[index])
        root.left = self.buildTree(arr, 2 * index + 1)
        root.right = self.buildTree(arr, 2 * index + 2)
        return root