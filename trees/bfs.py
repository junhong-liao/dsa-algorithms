from tree_node import TreeNode
# from collections import deque

def bfs(root: TreeNode) -> list[list[int]]:
    res = []
    if root: queue = collections.deque([root])
    while queue:
        length, level = len(queue), list()
        for i in range(length):
            treeNode = queue.popleft()
            level.append(treeNode.val)
            if treeNode.left: queue.append(treeNode.left)
            if treeNode.right: queue.append(treeNode.right)
        res.append(level)
    return res

# optimized

from typing import List, Optional
import collections

def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    res = [] 
    q = collections.deque()
    if root: q.append(root)

    while q:
        level = []
        for i in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        res.append(level)
    return res


#final

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = [] 
        q = collections.deque()
        if root: q.append(root)
        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(level)
        return res