from tree_node import TreeNode
from typing import Optional
from build_tree import TreeBuilder

def kth_smallest(root: Optional[TreeNode], k: int) -> int:
    # def search(root: Optional[TreeNode]) -> int:
    #     nonlocal k
    #     if not root: return None
    #     if (left := search(root.left)): return left
    #     if (k := k - 1) == 0: return root.val
    #     return search(root.right)

    def search(root: Optional[TreeNode]) -> int:
        nonlocal k
        if not root: return None
        print(root.val)
        left = search(root.left)
        if left != None: return left
        k -= 1
        if k == 0: return root.val
        return search(root.right)
    return search(root)

tb = TreeBuilder()
nodes = [31,30,48,3,None,38,49,0,16,35,47,None,None,None,2,15,27,33,37,39,None,1,None,5,None,22,28,32,34,36,None,None,43,None,None,4,11,19,23,None,29,None,None,None,None,None,None,40,46,None,None,7,14,17,21,None,26,None,None,None,41,44,None,6,10,13,None,None,18,20,None,25,None,None,42,None,45,None,None,8,None,12,None,None,None,None,None,24,None,None,None,None,None,None,9]
root = tb.construct_tree(nodes)
k = 1
res = kth_smallest(root, k)
print(f"result: {res}")