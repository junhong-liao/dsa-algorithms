from tree_node import TreeNode
from typing import Optional, List

'''
Able to solve with BFS
Build result containing the rightmost node of each level

'''
from collections import deque

# def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
#     res = [] 
#     q = deque()
#     if root: q.append(root)
#     while q:
#         level = []
#         for i in range(len(q)):
#             node = q.popleft()
#             level.append(node.val)
#             if node.left: q.append(node.left)
#             if node.right: q.append(node.right)
#         res.append(level)
#     return res

# def rightSideView(root: Optional[TreeNode]) -> List[int]:   
#     res = []
#     if not root: return res
#     q = deque([root])
#     while q:
#         nodes, length = [], len(q)
#         for i in range(length):
#             node = q.popleft() # DO NOT FORGET TO POPLEFT
#             nodes.append(node.val)
#             if node.left: q.append(node.left)
#             if node.right: q.append(node.right)
#         res.append(nodes)
#     # return [r[-1] for r in res]
#     return res

def rightSideView(root: Optional[TreeNode]) -> List[int]:
    res, q = list(), deque()
    if root: q.append(root)
    while q:
        length = len(q)
        target = None
        for i in range(length):
            target = q.popleft()
            if target.left: q.append(target.left)
            if target.right: q.append(target.right)
        res.append(target)
    return res