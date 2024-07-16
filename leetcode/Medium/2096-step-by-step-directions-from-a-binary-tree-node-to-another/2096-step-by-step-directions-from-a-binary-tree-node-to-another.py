# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getFromRoot(self, root, val):
        visited = set()
        stack = [(root, "")]
        while stack:
            node, d = stack.pop()
            if node.val == val:
                return d
            if node.left:
                stack.append((node.left, d + "L"))
            if node.right:
                stack.append((node.right, d + "R"))
        return ""

    def getDirections(
        self, root: Optional[TreeNode], startValue: int, destValue: int
    ) -> str:
        s = deque(self.getFromRoot(root, startValue))
        d = deque(self.getFromRoot(root, destValue))
        while s and d and s[0] == d[0]:
            s.popleft()
            d.popleft()
        return "U" * len(s) + "".join(d)
