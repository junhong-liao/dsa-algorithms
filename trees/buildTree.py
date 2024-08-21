from tree_node import TreeNode
from typing import Optional, List
from build_tree import TreeBuilder

def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]: 
    if not (preorder and inorder): return None
    root = TreeNode(preorder[0])
    mid = inorder.index(root.val)
    root.left = buildTree(preorder[1:mid+1], inorder[:mid+1])
    root.right = buildTree(preorder[mid+1:], inorder[mid+1:])
    return root

def in_order_traversal(root: Optional[TreeNode]) -> None:
    if not root: return
    in_order_traversal(root.left)
    print(root.val)
    in_order_traversal(root.right)

p = [10, 6, 14, 12, 11, 13, 16]
i = [6, 10, 11, 12, 13, 14, 16]
root = buildTree(p, i)
in_order_traversal(root)
