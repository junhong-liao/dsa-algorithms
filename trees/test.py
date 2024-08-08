# whitespace for code to test binary tree functions

from tree_node import TreeNode
from build_tree import TreeBuilder

# update tree method imports

from good_nodes import Solution

# update heap input here
treeBuilder = TreeBuilder()
s = Solution()
nodes = root=[-1,5,-2,4,4,2,-2,None,None,-4,None,-2,3,None,-2,0,None,-1,None,-3,None,-4,-3,3,None,None,None,None,None,None,None,3,-3]
root = treeBuilder.buildTree(nodes, 0)

# test function output
print(s.goodNodes(root))