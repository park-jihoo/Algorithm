# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        visited = set()
        m = dict()
        for p, c, l in descriptions:
            np, nc = m.setdefault(p, TreeNode(p)), m.setdefault(c, TreeNode(c))
            if l:
                np.left = nc
            else:
                np.right = nc
            visited.add(c)
        root = (set(m) - visited).pop()
        return m[root]
