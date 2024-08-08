from typing import Optional, List
from tree_node import TreeNode

class TreeBuilder:
    def __init__(self):
        pass
    
    def buildTree(self, arr: Optional[List[int]], index: int=0) -> Optional[TreeNode]:
        if index >= len(arr) or arr[index] == None: return None
        root = TreeNode(val=arr[index])
        root.left = self.buildTree(arr, 2 * index + 1)
        root.right = self.buildTree(arr, 2 * index + 2)
        return root
    
    def construct_tree(self, nodes):
        if not nodes:
            return None
        
        root = TreeNode(nodes[0])
        queue = [root]
        i = 1
        while queue and i < len(nodes):
            current = queue.pop(0)
            if nodes[i] is not None:
                current.left = TreeNode(nodes[i])
                queue.append(current.left)
            i += 1
            if i < len(nodes) and nodes[i] is not None:
                current.right = TreeNode(nodes[i])
                queue.append(current.right)
            i += 1
        return root
